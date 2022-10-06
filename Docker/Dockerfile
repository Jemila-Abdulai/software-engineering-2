FROM ubuntu:latest
FROM python:latest
RUN apt-get update -y
#RUN mkdir /opt/app
#COPY ../Backend/soil-moisture-sensor/requirements.txt /opt/app
COPY ./Backend/ /opt/Backend
ENTRYPOINT [ "/bin/bash" ]

## A note

# Currently, this is going to give us a decent container with Python on Ubuntu. 
# If we want our app to be in it we may need to change the dir structure so that everything is within the Docker folder. 
# This is due to how Dockerfiles work (everything needs to be inside the same dir)
# Another way is to copy the files we want in some way from outside to within the Docker dir. 