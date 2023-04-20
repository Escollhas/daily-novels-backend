resource "akeyless_static_secret" "cloudamqp_api_key" {
  path = "/cloudamqp_api_key"
  value = var.cloudamqp_api_key
}

resource "akeyless_static_secret" "cloudamqp_endpoint" {
  path = "/cloudamqp_endpoint"
  value = var.cloudamqp_endpoint
}

resource "akeyless_static_secret" "cloudamqp_username" {
  path = "/cloudamqp_username"
  value = var.cloudamqp_username
}

resource "akeyless_static_secret" "cloudamqp_password" {
  path = "/cloudamqp_password"
  value = var.cloudamqp_password
}