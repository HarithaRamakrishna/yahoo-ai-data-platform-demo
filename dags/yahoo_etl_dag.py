from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
  'owner' :'haritha',
  'depends_on_past' : False,
  'retries':1,
  'retry_delay': timedelta(minutes=5),

}

with DAG(
  dag_id ='yahoo_etl_dag',
  default_args =  default_args,
  description = 'Simulates Yahoo GCP-based data pipeline',
  schedule_interval = None,
  start_date = days_ago(1),
  catchup = False,
  tags=['yahoo','etl','gcp'],
) as dag:

  #Task 1: upload local file to GCS
  upload_to_gcs = BashOperator(
      task_id = 'upload_to_gcs',
      bash_command = 'echo "simulate upload user.csv to GCS..."'
  )
  #Task 2: Run Pyspark transformations
  run_pyspark_job = BashOperator(
    task_id = 'run_pyspark_job',
    bash_command = 'echo "Simulate Pyspark processing.."'
  )
  #Task3 : Load to Bigquery
  load_to_bigquery = BashOperator(
      task_id = 'load_to_bigquery',
      bash_command = 'echo "Load transformed data to BigQuery..."'
  )
  #Define task flow
  upload_to_gcs >> run_pyspark_job >> load_to_bigquery
    
    
  
  
