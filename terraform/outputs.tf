output "ec2_public_ip" {
  value = aws_instance.minikube_ec2.public_ip
}
