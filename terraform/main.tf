provider "aws" {
  region = "eu-west-1" 
}

resource "aws_key_pair" "deployer" {
  key_name   = "fraud-api-key"
  public_key = file("~/.ssh/id_rsa.pub") 
}

resource "aws_security_group" "fraud_api_sg" {
  name        = "fraud-api-sg"
  description = "Allow HTTP (8000) and SSH"

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "fraud_api" {
  ami           = "ami-0df368112825f8d8f"
  instance_type = "t2.micro"
  key_name      = aws_key_pair.deployer.key_name
  security_groups = [aws_security_group.fraud_api_sg.name]

  user_data = file("init.sh")

  tags = {
    Name = "fraud-api-server"
  }
  
}
