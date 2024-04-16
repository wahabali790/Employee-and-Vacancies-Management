from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import pyspark.sql.functions as F
import random

# Create a SparkSession
spark = SparkSession.builder \
    .appName("RandomDataFrameExample") \
    .getOrCreate()

# Generate random data
data = [("User" + str(i), random.choice(["Male", "Female"]), random.randint(18, 60), random.randint(1, 500)) for i in range(1, 101)]

# Define schema for the DataFrame
schema = StructType([
    StructField("name", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("friends", IntegerType(), True)
])

# Create DataFrame from random data and schema
df = spark.createDataFrame(data, schema)

# Apply aggregations
aggregated_df = df.groupBy("gender").agg(
    F.avg("age").alias("avg_age"),
    F.sum("friends").alias("total_friends")
)

# Show the aggregated DataFrame
print("Aggregated DataFrame:")
aggregated_df.show()

# Save the aggregated DataFrame
output_path = "hdfs:///user/maria_dev/spark/wahab_output/"
aggregated_df.write.mode("overwrite").parquet(output_path)

# Stop the SparkSession
spark.stop()

