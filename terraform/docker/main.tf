terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.23.1"
    }
  }
}

provider "docker" {
    #host = "tcp://localhost:2375" # -- Windows
    host = "unix:///var/run/docker.sock" # -- Linux
}

resource "docker_image" "daily-novels-api-image" {
  name = "daily-novels-api-image:latest"
  build {
    path = "../.."
    label = {
      author : "@escollhas"
    }
  }
}

resource "docker_container" "daily-novels-api-container" {
  name  = "daily-novels-api-container"
  image = docker_image.daily-novels-api-image.image_id

  ports {
    external = 80
    internal = 80
  }
}