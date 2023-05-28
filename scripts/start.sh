docker build -t python-lambda-sqs .
docker exec -it $(docker run -v  $(pwd):/code  -d python-lambda-sqs) /bin/bash