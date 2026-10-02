locals {
  project_name = var.project_name
  environment  = var.environment

  infrastructure = {
    application = "order-service"
    replicas    = var.replica_count
    port        = var.application_port

    containerization = "Docker"
    orchestration    = "Kubernetes"
    packaging        = "Helm"
    monitoring       = "Prometheus"
    dashboards       = "Grafana"
    alerting         = "Alertmanager"
    automation       = "Python"
  }
}