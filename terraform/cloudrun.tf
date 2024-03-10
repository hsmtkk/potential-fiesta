resource "google_secret_manager_secret" "openai_api_key" {
  secret_id = "openai-api-key"
  replication {
    auto {
    }
  }
}

resource "google_secret_manager_secret_version" "secret_version" {
  secret      = google_secret_manager_secret.openai_api_key.id
  secret_data = "placeholder"
}


resource "google_service_account" "front" {
  account_id = "front-runner"
}

resource "google_project_iam_member" "project" {
  project = var.project_id
  role    = "roles/secretmanager.secretAccessor"
  member  = "serviceAccount:${google_service_account.front.email}"
}

resource "google_cloud_run_v2_service" "front" {
  location = var.region
  name     = "front"
  template {
    containers {
      env {
        name = "OPENAI_API_KEY"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.openai_api_key.id
            version = "latest"
          }
        }
      }
      image = "us-docker.pkg.dev/cloudrun/container/hello" # will be override by cloudbuild
    }
    service_account = google_service_account.front.email
  }
}

data "google_iam_policy" "noauth" {
  binding {
    role    = "roles/run.invoker"
    members = ["allUsers"]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location    = google_cloud_run_v2_service.front.location
  project     = google_cloud_run_v2_service.front.project
  service     = google_cloud_run_v2_service.front.name
  policy_data = data.google_iam_policy.noauth.policy_data
}
