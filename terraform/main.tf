resource "aws_vpc" "patient_vpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "patient-vpc"
  }
}

resource "aws_subnet" "patient_subnet" {
  vpc_id            = aws_vpc.patient_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "patient-subnet"
  }
}

resource "aws_instance" "minikube_ec2" {
  ami                         = "ami-051f8a213df8bc089" # Amazon Linux 2 في us-east-1
  instance_type               = "t2.medium"
  subnet_id                   = aws_subnet.patient_subnet.id
  associate_public_ip_address = true
  key_name                    = "your-key-name" # غيرها لو عندك key pair

  tags = {
    Name = "minikube-ec2"
  }
}
