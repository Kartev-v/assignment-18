# assignment-18

## Objective
Create a DataFrame containing 5 million records using spark.range().
Display initial partitions, increase partitions using repartition(),
and reduce partitions using coalesce().

## Build Docker Image
docker build -t pyspark-demo .

## Run Container
docker run pyspark-demo