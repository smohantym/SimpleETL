from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

# Initialize Spark Session
spark = SparkSession.builder.appName("SimpleETL").getOrCreate()

# Extract
input_path = "/data/sales.csv"
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Transform
result = df.groupBy("category").agg(spark_sum(col("amount")).alias("total_sales"))

# Optional: coalesce to a single output file for demo convenience
result = result.coalesce(1)

# Load
output_dir = "/data/output/csv"
result.write.mode("overwrite").csv(output_dir, header=True)

print("✅ ETL job completed successfully! Output:", output_dir)

spark.stop()
