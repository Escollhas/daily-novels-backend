data "akeyless_static_secret" "cloudamqp_endpoint" {
  path = "cloudamqp_endpoint"
}

data "akeyless_static_secret" "cloudamqp_username" {
  path = "cloudamqp_username"
}

data "akeyless_static_secret" "cloudamqp_password" {
  path = "cloudamqp_password"
}

resource "rabbitmq_queue" "makeawish" {
  name  = "makeawish"
  vhost = data.akeyless_static_secret.cloudamqp_username.value

  settings {
    durable     = false
    auto_delete = true
    arguments   = {
      "x-queue-type" : "classic",
    }
  }
}

resource "rabbitmq_queue" "makeawish2" {
  name  = "makeawish2"
  vhost = data.akeyless_static_secret.cloudamqp_username.value

  settings {
    durable     = false
    auto_delete = true
    arguments   = {
      "x-queue-type" : "classic",
    }
  }
}