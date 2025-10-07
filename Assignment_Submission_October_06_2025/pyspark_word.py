from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("WordCountApp") \
    .getOrCreate()

# Read text file(s)
text_file = spark.sparkContext.textFile(r"C:\Users\Sreeja\Training-submissions-1\Assignment_Submission_October_06_2025\Sampletxt.txt")


# Split each line into words
words = text_file.flatMap(lambda line: line.split(" "))

# Map each word to (word, 1)
word_pairs = words.map(lambda word: (word.lower(), 1))

# Reduce by key to count occurrences
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

# Sort by count (descending)
sorted_counts = word_counts.sortBy(lambda x: x[1], ascending=False)

# Collect results
for word, count in sorted_counts.collect():
    print(f"{word}: {count}")

# Stop the Spark session
spark.stop()
