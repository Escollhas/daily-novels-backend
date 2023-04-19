## Version 3> is failing in docker local
## Some bug in Windows cant read Dockerfil test: https://github.com/docker/buildx/issues/426#issuecomment-732980948
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.23.1"
    }
  }
}

provider "docker" {
    ## TO Linus should be host = "unix:///var/run/docker.sock"
    #host = "tcp://localhost:2375"
    host = "unix:///var/run/docker.sock"
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