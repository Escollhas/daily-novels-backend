terraform {
  required_providers {
    akeyless = {
      version = ">= 1.0.0"
      source = "akeyless-community/akeyless"
    }
  }
}

provider "akeyless" {
  api_key_login {
    access_id = var.access_id
    access_key = var.access_key
  }
}