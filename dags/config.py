
data_source_path = '/usr/local/airflow/dags/data/Students.csv'
gcs_bucket_name = 'eniola_students_data_bucket'
gcs_file_name = 'students.csv'

project_id = 'de-project-495521'


schema_fields = [
    {"name": "student_id", "type": "STRING", "mode": "NULLABLE"},
    {"name": "first_name", "type": "STRING", "mode": "NULLABLE"},
    {"name": "last_name", "type": "STRING", "mode": "NULLABLE"},
    {"name": "gender", "type": "STRING", "mode": "NULLABLE"},
    {"name": "department", "type": "STRING", "mode": "NULLABLE"},
    {"name": "enrollment_date", "type": "STRING", "mode": "NULLABLE"},
    {"name": "gpa", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "status", "type": "STRING", "mode": "NULLABLE"},
]