# Google storage account
resource "google_storage_bucket" "students_data" {
  name          = "eniola_students_data_bucket"
  location      = var.region
  force_destroy = true

  uniform_bucket_level_access = true
}

resource "google_bigquery_dataset" "eniola_students_data_dataset" {
  dataset_id                  = "eniola_students_data_dataset"
  friendly_name               = "students_data_dataset"
  description                 = "This dataset contains student data"
  location                    = "EU"
  default_table_expiration_ms = 3600000

}

resource "google_bigquery_table" "students_table" {
  dataset_id = google_bigquery_dataset.eniola_students_data_dataset.dataset_id
  table_id   = "students_data"

  deletion_protection = false

  schema = local.table_schema
}