import os
import sys
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
from pyspark.sql.functions import sum, avg

spark = SparkSession.builder.appName("Marks").getOrCreate()

data = [("Giri", 80), ("Arun", 90), ("Kumar", 70)]

df = spark.createDataFrame(data, ["name", "mark"])

df.show()

df.select(
    sum("mark").alias("total"),
    avg("mark").alias("average")
).show()

spark.stop()