# Configure the AWS Provider
variable "access_key" {}
variable "secret_key" {}

variable "aws_region" {
  description = "The AWS region to create things in."
  default = "ap-northeast-1"
}

/* Ubuntu 14.04 amis by region */
variable "aws_amis" {
  default = {
    "ap-northeast-1" = "ami-d82efcb9"
  }
}

variable "key_name" {
  default = "aws_lambda_chatbot.pem"
  description = "Name of the SSH keypair to use in AWS."
}
