include .env

build:
	docker build -t ${APP_NAME} .

run:
	docker run -it --rm --name ${APP_NAME} ${APP_NAME} bash

