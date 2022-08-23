output "gitlab_external_ip" {
  value = yandex_compute_instance.gitlab.network_interface[0].nat_ip_address
}

output "gitlab_runner_external_ip" {
  value = yandex_compute_instance.gitlab_runner.network_interface[0].nat_ip_address
}

output "staging_external_ip" {
  value = yandex_compute_instance.staging.network_interface[0].nat_ip_address
}

output "production_external_ip" {
  value = yandex_compute_instance.production.network_interface[0].nat_ip_address
}
