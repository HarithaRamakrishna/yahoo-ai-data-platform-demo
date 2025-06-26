from pyspark.sql import SparkSession
from pyspark.sql.functions import (to_date, when, col, datediff, current_date, count as _count)

#Create SparkSession
spark = SparkSession.builder \
        .appName("YahooUserEnrichment") \
        .getOrCreate()
        
#Read Raw data
users_df = spark.read.csv("data/users.csv", header=True, inferSchema=True)
events_df = spark.read.csv("data/clickstram.csv", header=True, inferSchema = True)



#Data Cleaning & Transformation
users_clean = (
        users_df
        .withColumn("signup_date", to_date(col("signup_ts"))) 
        .withColumn("region", when(col("region").isNull(),"unknown").otherwise(col("region"))) 
         .withColumn("days_active", datediff(current_date(), col("signup_date")))
)

#Aggregate events per user
events_agg = (
    events_df
    .groupby("user_id")
    .agg(
        _count("*").alias("total_events"),
        _count("session_id").alias("total_sessions")
    )
)

#join users and events
enriched = users_clean.join(event_agg, on='user_id', how = 'left') \
        .na.fill({"total_events": 0, "total_sessions":0})

#Show transformed data
enriched.show(10, False)
#Write to output
enriched.write.mode("overwrite").parquet("data/processed_users")


