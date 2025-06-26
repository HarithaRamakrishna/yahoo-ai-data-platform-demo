# Yahoo AI Data Platform Demo 

A hands-on, end-to-end data engineering project designed to simulate a real-world data pipeline like those used by Yahoo's Consumer Data Team — focusing on scalable ingestion, transformation, and preparation for AI/ML use cases.


## Project Overview

This project demonstrates how to:

- Ingest raw user engagement data into a cloud data lake  
- Process and transform the data using PySpark  
- Build dbt models for analytics and AI-ready data  
- Orchestrate workflows with Apache Airflow  
- Store data efficiently in Google BigQuery  

## Architecture

1. Raw data: CSV files in `/data`  
2. Orchestration: Airflow DAG `yahoo_etl_dag.py`  
3. Transform: PySpark script `preprocess_pyspark.py`  
4. Enriched output: Parquet in `/data/enriched_users`  
5. Modeling: `dbt/models/user_behavior.sql`  
6. Final tables: Deployed to BigQuery
