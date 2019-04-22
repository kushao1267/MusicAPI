include .env

build:
	docker build -t ${APP_NAME} .

run:
	docker run -it --rm --name ${APP_NAME} -e "APP_ENV=${APP_ENV}" -v "${PWD}":/opt/app ${APP_NAME}

exec:
	docker exec -it ${APP_NAME} bash

shell:
	docker exec -it ${APP_NAME} manage.py shell
