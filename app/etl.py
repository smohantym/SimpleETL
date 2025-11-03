from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

# Initialize Spark
spark = SparkSession.builder.appName("SimpleETL").getOrCreate()

# Extract
df = spark.read.csv("/data/sales.csv", header=True, inferSchema=True)

# Transform
result = df.groupBy("category").agg(spark_sum(col("amount")).alias("total_sales"))

# Load
result.write.mode("overwrite").csv("/data/output", header=True)

print("✅ ETL job completed successfully!")

spark.stop()
