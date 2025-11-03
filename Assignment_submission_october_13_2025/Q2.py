from typing import List, Tuple, Optional
import statistics

def mean_median(values: List[float]) -> Tuple[Optional[float], Optional[float]]:
    """
    Returns (mean, median) for a list of numbers.
    Returns (None, None) for an empty list.
    """
    if not values:
        return None, None

    # mean: sum / n (computed exactly)
    n = len(values)
    total = 0.0
    for v in values:
        total += float(v)
    mean_val = total / n

    # median: use sorting and handle even/odd
    sorted_vals = sorted(values)
    mid = n // 2
    if n % 2 == 1:
        median_val = float(sorted_vals[mid])
    else:
        median_val = (float(sorted_vals[mid - 1]) + float(sorted_vals[mid])) / 2.0

    return mean_val, median_val

# Example usage
data1 = [10, 20, 30, 40, 50]
data2 = [3, 1, 4, 2]
print("data1:", mean_median(data1))  # (30.0, 30.0)
print("data2:", mean_median(data2))  # (2.5, 2.5)
print("empty:", mean_median([]))     # (None, None)
