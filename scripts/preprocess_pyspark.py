from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, when, col, datediff, current_date

#Create SparkSession
spark = SparkSession.builder \
        .appName("YahooUserPreprocessing") \
        .getorCreate()
        
#Read Raw data
df = spark.read.csv("data/users.csv", header=True, inferSchema=True)

#Data Cleaning & Transformation
df_clean = df.withColumn("signup_date", to_date(col("signup_ts"))) \
             .withColumn("region", when(col("region").isNull(),"unknown").otherwise(col("region"))) \
             .withColumn("days_active", datediff(current_date(), col("signup_date")))

#Show transformed data
df_clean.show()
#Write to output
df_clean.write.mode("overwrite").parquet("data/processed_users")   
