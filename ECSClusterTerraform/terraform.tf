terraform {
  backend "s3" {
    bucket = "terraformbucketapp"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }
}