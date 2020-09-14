FROM python:3.6-alpine3.7
RUN apk add --no-cache mariadb-dev build-base
ENV PYTHONUNBUFFERED=0
WORKDIR /project
ADD . /project
# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait 
RUN pip install -r requirements.txt
