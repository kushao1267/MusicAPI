FROM python:3.6.5-slim as build

RUN apt-get update && apt-get install -y make

WORKDIR /opt/app

#RUN pip install mozart

FROM python:3.6.5-slim

LABEL maintainer="krusjra <jianliu001922@gmail.com>"

COPY . .

RUN pip install -r requirements.txt
#EXPOSE 8080

CMD python -m mozart