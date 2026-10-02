output "project_name" {
  description = "Project name"
  value       = local.project_name
}

output "environment" {
  description = "Deployment environment"
  value       = local.environment
}

output "application_name" {
  description = "Application managed by the infrastructure"
  value       = local.infrastructure.application
}

output "replica_count" {
  description = "Configured application replicas"
  value       = local.infrastructure.replicas
}

output "application_port" {
  description = "Application port"
  value       = local.infrastructure.port
}