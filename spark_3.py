import os
import sys

# Automatically set JAVA_HOME and HADOOP_HOME if not present in the current terminal environment
if "JAVA_HOME" not in os.environ:
    java_path = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot"
    if os.path.exists(java_path):
        os.environ["JAVA_HOME"] = java_path
        os.environ["PATH"] = os.path.join(java_path, "bin") + ";" + os.environ.get("PATH", "")

if "HADOOP_HOME" not in os.environ:
    hadoop_path = r"C:\hadoop"
    if os.path.exists(hadoop_path):
        os.environ["HADOOP_HOME"] = hadoop_path
        os.environ["PATH"] = os.path.join(hadoop_path, "bin") + ";" + os.environ.get("PATH", "")

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ParquetETL").getOrCreate()

# create sample data
data = [
    (101, "Laptop", 50000),
    (102, "Mobile", 20000),
    (103, "Tablet", 15000)
]

df = spark.createDataFrame(data, ["id", "product", "price"])

# write data to parquet file
df.write.mode("overwrite").parquet("sales.parquet")

# read parquet file
df2 = spark.read.parquet("sales.parquet")

# display data
df2.show()

# filter expensive products
df2.filter(df2.price > 18000).show()

spark.stop()