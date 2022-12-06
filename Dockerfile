FROM python:latest

WORKDIR /usr/app
COPY influx.py .
RUN apt -y update && apt -y upgrade
RUN apt install -y python3-pip
RUN pip3 install psutil
RUN pip3 install influxdb
CMD [ "python3", "influx.py" ]
