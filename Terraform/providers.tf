terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 7.34.0"
    }
  }
}


provider "google" {
  project = "de-project-495521"
  region  = "africa-south1"
  zone    = "africa-south1-b"
}