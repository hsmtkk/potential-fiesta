resource "google_artifact_registry_repository" "registry" {
  location      = var.region
  repository_id = "registry"
  format        = "DOCKER"
}
