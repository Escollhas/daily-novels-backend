terraform {
  required_providers {
    akeyless = {
      version = ">= 1.0.0"
      source = "akeyless-community/akeyless"
    }
    rabbitmq = {
      version = ">= 1.8.0"
      source = "cyrilgdn/rabbitmq"
    }
  }
}

provider "akeyless" {
  api_key_login {
    access_id = var.access_id
    access_key = var.access_key
  }
}

provider "rabbitmq" {
  endpoint = data.akeyless_static_secret.cloudamqp_endpoint.value
  username = data.akeyless_static_secret.cloudamqp_username.value
  password = data.akeyless_static_secret.cloudamqp_password.value
}