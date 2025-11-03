# Hard: mini inventory system
from typing import Dict, Any, Optional, List

Inventory = Dict[str, Dict[str, Any]]

def create_inventory() -> Inventory:
    return {}

def add_item(inv: Inventory, sku: str, name: str, qty: int, price: float, location: str = "default") -> None:
    """
    Add new item or increase quantity if SKU exists.
    """
    if sku in inv:
        inv[sku]["qty"] += qty
    else:
        inv[sku] = {
            "name": name,
            "qty": qty,
            "price": float(price),
            "location": location,
        }

def remove_item(inv: Inventory, sku: str, qty: int) -> bool:
    """
    Remove quantity from an item. Returns True if successful, False if not enough stock or missing.
    If qty reduces to 0 or less, deletes the item.
    """
    if sku not in inv:
        return False
    if inv[sku]["qty"] < qty:
        return False
    inv[sku]["qty"] -= qty
    if inv[sku]["qty"] <= 0:
        del inv[sku]
    return True

def update_item(inv: Inventory, sku: str, *, name: Optional[str]=None,
                price: Optional[float]=None, location: Optional[str]=None) -> bool:
    if sku not in inv:
        return False
    if name is not None:
        inv[sku]["name"] = name
    if price is not None:
        inv[sku]["price"] = float(price)
    if location is not None:
        inv[sku]["location"] = location
    return True

def get_item(inv: Inventory, sku: str) -> Optional[Dict[str, Any]]:
    return inv.get(sku)

def search_by_name(inv: Inventory, q: str) -> List[Dict[str, Any]]:
    q_lower = q.lower()
    results = []
    for sku, meta in inv.items():
        if q_lower in meta["name"].lower():
            entry = {"sku": sku, **meta}
            results.append(entry)
    return results

def inventory_report(inv):
    total_value = 0.0
    # Column headers with spacing
    print(f"{'SKU':<10} {'Name':<15} {'Qty':<8} {'Price':<10} {'Location':<12} {'Value':<10}")
    print("-" * 70)

    for sku, meta in sorted(inv.items()):
        value = meta['qty'] * meta['price']
        total_value += value
        print(f"{sku:<10} {meta['name']:<15} {meta['qty']:<8} "
              f"${meta['price']:<9.2f} {meta['location']:<12} ${value:<9.2f}")

    print("-" * 70)
    print(f"{'Total inventory value:':<60} ${total_value:.2f}")


# Example usage
if __name__ == "__main__":
    inv = create_inventory()

    add_item(inv, "SKU001", "Widget A", 100, 2.50, "Aisle 1")
    add_item(inv, "SKU002", "Widget B", 50, 5.00, "Aisle 2")
    add_item(inv, "SKU003", "Gadget", 10, 25.00, "Shelf 4")

    print("Initial report:")
    inventory_report(inv)

    print("\nSell 3 of SKU001 and 2 of SKU003")
    remove_item(inv, "SKU001", 3)
    remove_item(inv, "SKU003", 2)

    print("\nAfter sales report:")
    inventory_report(inv)

    print("\nSearch for 'widget':")
    print(search_by_name(inv, "widget"))

    print("\nUpdate SKU002 price and location:")
    update_item(inv, "SKU002", price=4.75, location="Aisle 3")
    inventory_report(inv)
