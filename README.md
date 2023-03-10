# my-first-flask-app
A simple flask application for Design and Architecture class

## Installation

Build docker image
```bash
docker build -t my-first-flask-app .
```

## Usage
Run a docker container
```bash
docker run -p 5000:5000 my-first-flask-app
```
Access the app at http://localhost:5000/