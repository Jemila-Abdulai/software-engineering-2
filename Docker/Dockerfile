FROM ubuntu:latest
FROM python:latest
RUN apt-get update -y
COPY ./sensors/ /opt/sensors
COPY ./dashboard /opt/dashboard
COPY ./util /opt/util
RUN ["pip", "install", "Counterfit"]
RUN ["pip", "install", "counterfit_connection"]
CMD ["python", "/opt/util/waiting.py"]

# No longer needed but want to keep as 
# part of my notes for now:
#ENTRYPOINT [ "/bin/bash" ]

