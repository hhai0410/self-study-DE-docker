variable "project" {
  description = "Project"
  default     = "terraform-demo-503509"
}
variable "location" {
  description = "Project Location"
  default     = "asia-southeast1"
}
variable "credential" {
  description = "Credential Authorization"
  default = "./keys/terraform-demo-503509-36e277310a0d.json"
}
variable "region" {
  description = "Project Region"
  default     = "asia-southeast1"
}
variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "terraform-demo-503509-terraform-bucket"
}
variable "dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}
variable "gcs_bucket_class" {
  description = "My Storage Bucket Class"
  default     = "STANDARD"
}