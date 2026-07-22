from datetime import datetime, timedelta
from config import (
  schema_fields, data_source_path, 
  gcs_bucket_name, gcs_file_name, project_id
)
from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
    GCSToBigQueryOperator
)
from airflow.providers.google.cloud.transfers.local_to_gcs import (
    LocalFilesystemToGCSOperator
)

default_args = {
    'owner': 'eniola',
    'depends_on_past': False,
    'start_date': datetime(2026, 7, 18),
    'retries': 1,
    'retry_delay': timedelta(minutes=3)
}


with DAG(dag_id='gcs_bq_dag', schedule='@hourly',
         catchup=False, default_args=default_args) as dag: 


  upload_csv_file_to_gcs = LocalFilesystemToGCSOperator(
        task_id ="upload_csv_file",
        bucket=gcs_bucket_name,
        src= data_source_path,
        dst=gcs_file_name
    ) 
  
  load_gcs_to_bq = GCSToBigQueryOperator(
    task_id="load_gcs_to_bq",
    bucket=gcs_bucket_name, 
    source_objects=[gcs_file_name],
    destination_project_dataset_table=f"{project_id}.eniola_students_data_dataset.students_data",
    schema_fields=schema_fields,
    source_format="CSV",
    write_disposition="WRITE_TRUNCATE",
    autodetect=False,
    skip_leading_rows=1,
  )


( 
    upload_csv_file_to_gcs
    >> load_gcs_to_bq
)