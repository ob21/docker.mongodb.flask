https://www.youtube.com/watch?v=6opltZu4ABw


# Docker version
docker version


# Docker Compose version
docker compose version


# Docker commands
sudo docker images #List images
sudo docker image prune -a #Remove unused containers and images
sudo docker image rm <image-id> #Remove an image
sudo docker container stats #Stats on running containers
sudo docker container top <container-id> #Running processes of a container
sudo docker container logs <container-id> #Logs of a container
sudo docker container ls #List containers
sudo docker container inspect <container-id> | grep IPAddress #See IP address of a container


# Create files
touch app.py
touch config.py
touch templates
touch templates/todo.html
touch Dockerfile
touch docker-compose.yml
touch requirements.txt


# Write app.py
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def todo():
        return "Hello!"

@app.route('/new', methods=['POST'])
def new():
        return redirect(url_for('todo'))

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)


# Write requirements.txt
flask
pymongo


# Write Dockerfile
FROM python:2.7
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt


# Write docker-compose.yml
web:
  build: .
  command: python -u app.py
  ports:
    - "5000:5000"
  volumes:
    - .:/todo


# Start docker-compose
sudo docker-compose up
sudo docker-compose up --remove-orphans


# Look at the server
http://0.0.0.0:5000
