variable "project_name" {
  description = "Name of the SRE automation project"
  type        = string
  default     = "sre-automation-platform"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "production"
}

variable "replica_count" {
  description = "Number of application replicas"
  type        = number
  default     = 2
}

variable "application_port" {
  description = "Application container port"
  type        = number
  default     = 8000
}