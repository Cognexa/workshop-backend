create_venv:
	python3 -m venv .venv

venv:
	# if .venv directory does not exist, create it
	if [ ! -d ".venv" ]; then make create_venv; fi
	# activate the virtual environment and install the requirements
	. .venv/bin/activate && pip install -r requirements.txt

run:
	if [ ! -d ".venv" ]; then make venv; fi
	. .venv/bin/activate && gunicorn main:app -b "0.0.0.0:5000"

test-get:
	# test the applications endpoint by sending a GET request
	curl -X GET http://localhost:5000/get

test-post:
	# test the applications endpoint by sending a POST request
	curl -X POST http://localhost:5000/post -H "Content-Type: application/json" -d '{"key": "value"}'

build:
	# build the docker image, --rm removes intermediate containers after a successful build
	# --pull always attempts to pull a newer version of the base image
	# -f specifies the Dockerfile to use
	# -t specifies the tag for the image
	docker build --pull --rm -f 'Dockerfile' -t 'backendworkshop-flask:latest' '.' 

up:
	# run the docker container, -d runs the container in the background
	# -p specifies the port mapping, host_port:container_port
	# --name specifies the name of the container
	# --rm removes the container when it is stopped
	docker run --rm -it -p 5000:5000/tcp backendworkshop-flask:latest

clean:
	rm -rf .venv
	# force remove the docker image
	docker rmi -f backendworkshop-flask

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@echo "  run          Run the Flask application"
	@echo "  test-get     Test the GET endpoint"
	@echo "  test-post    Test the POST endpoint"
	@echo "  build        Build the Docker image"
	@echo "  up           Run the Docker container"
	@echo "  clean        Remove the virtual environment and Docker image"
	@echo "  help         Display this help message"
	
.PHONY: run create_venv venv