from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PartitionDemo") \
    .getOrCreate()

df = spark.range(5000000)

print("initial no. of partitions:", df.rdd.getNumPartitions())

df_repartitioned = df.repartition(12)
print("no. of partitions after repartitions:", df_repartitioned.rdd.getNumPartitions())

df_coalesced = df_repartitioned.coalesce(3)
print("no. of partitions after coalesce:", df_coalesced.rdd.getNumPartitions())

df_coalesced.show(5)

spark.stop()