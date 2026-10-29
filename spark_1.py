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
spark = SparkSession.builder.appName("SimpleExample").getOrCreate()
data = [
    (1, "giri", 85),
    (2, "arun", 90),
    (3, "kumar", 75)
]
columns = ["id", "name", "mark"]
df = spark.createDataFrame(data, columns)
df.show()
df.filter(df.mark > 80).show()
spark.stop()