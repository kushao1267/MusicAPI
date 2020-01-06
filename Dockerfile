FROM python:3.6.5-slim

LABEL maintainer="krusjra <jianliu001922@gmail.com>"

COPY . .

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider --no-cache-dir -r requirements.txt
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone 
#EXPOSE 8080

CMD python -m mozart
