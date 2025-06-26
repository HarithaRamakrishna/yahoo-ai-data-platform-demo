# Yahoo AI Data Platform Demo 

a)Problem Statement:
Modern AI/ML models depend on fresh, clean, and well-engineered features. This demo simulates how Yahoo’s Consumer Data Team might ingest high-volume clickstream data, perform complex transformations (handling missing values, geo-enrichment, sessionization), and surface it for downstream AI pipelines—addressing challenges of data freshness, scale, and feature reproducibility.


b)Project Overview

This project demonstrates how to:

- Ingest raw user engagement data into a cloud data lake  
- Process and transform the data using PySpark  
- Build dbt models for analytics and AI-ready data  
- Orchestrate workflows with Apache Airflow  
- Store data efficiently in Google BigQuery  

c) Data Pipeline Architecture

graph LR
    A[Clickstream CSV in GCS/S3] --> B{Raw Layer/Landing Zone}
    B --> C[Airflow DAG]
    C --> D[PySpark Transform (Clean & Enrich)]
    D --> E[Staging Tables in BigQuery]
    E --> F[dbt Models (SQL Transforms in BQ)]
    F --> G[BigQuery Tables (Mart/Final)]
    G --> H[AI Model Training/Serving]
    
d) Data Sources & Schema 

 Data Schema
 
 users.csv
| Column     | Type    | Description                    |
|------------|---------|--------------------------------|
| user_id    | integer | Unique user identifier         |
| signup_ts  | date    | Signup timestamp               |
| region     | string  | User region code (US, IN, etc) |
| device     | string  | Device type (mobile, desktop)  |
| referrer   | string  | Acquisition channel            |

 clickstream.csv
| Column     | Type      | Description                           |
|------------|-----------|---------------------------------------|
| event_id   | string    | Unique event identifier (`e00001`)    |
| user_id    | integer   | Foreign key to `users.csv`            |
| timestamp  | datetime  | Event timestamp                       |
| page       | string    | Page URL path (e.g., `/news`)         |
| event_type | string    | Action type (click, scroll, hover)    |
| session_id | string    | Session grouping identifier           |

e) Transformations & Logic
1. Data Cleaning (PySpark):*
   - Convert `signup_ts` to `signup_date`  
   - Fill missing `region` with `"unknown"`  
   - Calculate `days_active`  

2. Feature Engineering (PySpark + dbt):
   - Aggregate total events & sessions per user  
   - Sessionization and event counts  
   - (Future) Geo-enrichment via IP lookup  

3. Modeling (dbt):
   - `user_behavior` model creates AI-ready features  
   - Materialized as tables for downstream modeling

f) Scalability & Performance Consideration
Scalability:
For real-world volumes (billions of events/day), we’d partition clickstream by event date and region, leverage Spark on a multi-node cluster (e.g., Dataproc with autoscaling), and push parquet files into partitioned GCS buckets. dbt models would also use incremental loads to avoid full rebuilds.

g) Error Handling & Monitoring

PySpark jobs wrapped in try/except, with logs emitted to Stackdriver Logging

Airflow tasks use SLA callbacks and email alerts on failures

Metrics (throughput, latency) sent to Prometheus and visualized in Grafana

dbt test suite validates data quality before materialization

h) Future Enhancements

Streaming ingestion with Pub/Sub or Kafka

Integration with a Feature Store (e.g., Feast)

Model training pipeline via MLflow + Vertex AI

Containerized deployment on Kubernetes with CI/CD

h) Contribution & License

How to Contribute:
Pull requests welcome; please follow the Contribution Guidelines for code style.

License:
This project is licensed under the MIT License.

