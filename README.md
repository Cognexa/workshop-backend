# Backend Workshop

Welcome to the Backend Workshop! This repository contains a FastAPI application designed to help you learn and practice backend development with Python and Docker.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Getting Started

**Clone the repository:**

```sh
git clone https://github.com/yourusername/backend-workshop.git
cd backend-workshop
```

### Running the FastAPI Application
```sh
cd fastapi
make run
```

### Running the Flask Application
```sh
cd flask
make run
```

Simple as that! You now have a FastAPI application running on `http://localhost:8000` or a Flask application running on `http://localhost:5000`.

## Project Structure
```sh
.
├── docker-compose.yaml  # Docker Compose configuration
├── .gitignore           # Git ignore file
├── fastapi              # FastAPI application
│   ├── Dockerfile       # Dockerfile for the FastAPI application
│   ├── main.py          # FastAPI application code
│   ├── Makefile         # Makefile for common tasks
│   └── requirements.txt # Python dependencies
├── flask                # Flask application (coming soon)
│   ├── Dockerfile       # Dockerfile for the Flask application
│   ├── main.py          # Flask application code
│   ├── Makefile         # Makefile for common tasks
│   └── requirements.txt # Python dependencies
└── README.md            # this README
```

## Contributing
We welcome contributions! Please fork the repository and submit a pull request with your changes.