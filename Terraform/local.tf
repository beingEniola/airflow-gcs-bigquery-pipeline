locals {
  table_schema = jsonencode([
    {
      name        = "student_id"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Unique identifier assigned to each student"
    },
    {
      name        = "first_name"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Student's first name"
    },
    {
      name        = "last_name"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Student's last name"
    },
    {
      name        = "gender"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Gender of the student"
    },
    {
      name        = "department"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Academic department in which the student is enrolled"
    },
    {
      name        = "enrollment_date"
      type        = "DATE"
      mode        = "NULLABLE"
      description = "Date the student enrolled in the institution"
    },
    {
      name        = "gpa"
      type        = "FLOAT"
      mode        = "NULLABLE"
      description = "Student's cumulative Grade Point Average"
    },
    {
      name        = "status"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Current enrollment status of the student (e.g., Active, Inactive, Graduated)"
    }
  ])
}