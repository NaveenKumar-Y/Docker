

docker build -t fastapi:v1 .

docker run -p 8000:8000 fastapi:v1


# to push to ECR (repo : dev_ecr_repo)

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 708735187026.dkr.ecr.us-east-1.amazonaws.com

docker tag fastapi:v1 708735187026.dkr.ecr.us-east-1.amazonaws.com/dev_ecr_repo:v1

docker push 708735187026.dkr.ecr.us-east-1.amazonaws.com/dev_ecr_repo:v1
