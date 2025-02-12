venv:
	# if .venv directory does not exist, create it
	if [ ! -d ".venv" ]; then python3 -m venv .venv; fi
	# activate the virtual environment and install the requirements
	. .venv/bin/activate && pip install -r requirements.txt

run:
	if [ ! -d ".venv" ]; then make venv; fi
	. .venv/bin/activate && uvicorn main:app --reload

test-get:
	# test the applications endpoint by sending a GET request
	curl -X GET http://localhost:8080/get

test-post:
	# test the applications endpoint by sending a POST request
	curl -X POST http://localhost:8080/post -H "Content-Type: application/json" -d '{"name": "Palko", "age": 25}'

test-speed:
	# test the applications endpoint by sending a GET request 1000 times
	# -n 1 specifies the number of arguments to pass to curl
	# -P 1000 specifies the number of parallel processes to run
	# /dev/null is a special file that discards all data written to it
	seq 1 1000 | xargs -n 1 -P 1000 -I {} sh -c 'curl -s http://localhost:8080/speed/{}'

build:
	# build the docker image, --rm removes intermediate containers after a successful build
	# --pull always attempts to pull a newer version of the base image
	# -f specifies the Dockerfile to use
	# -t specifies the tag for the image
	docker build --pull --rm -f 'Dockerfile' -t 'backendworkshop-fastapi:latest' '.' 

up:
	# run the docker container, -d runs the container in the background
	# -p specifies the port mapping, host_port:container_port
	# --name specifies the name of the container
	# --rm removes the container when it is stopped
	docker run --rm -it -p 8080:8080/tcp backendworkshop-fastapi:latest 

clean:
	rm -rf .venv
	# force remove the docker image
	docker rmi -f backendworkshop-fastapi

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@echo "  run          Run the FastAPI application"
	@echo "  test-get     Test the GET endpoint"
	@echo "  test-post    Test the POST endpoint"
	@echo "  test-speed   Test the speed endpoint"
	@echo "  build        Build the Docker image"
	@echo "  up           Run the Docker container"
	@echo "  clean        Remove the virtual environment and Docker image"
	@echo "  help         Display this help message"
	
.PHONY: run create_venv venv