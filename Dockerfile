FROM python:3.11.1-alpine

RUN mkdir -p /home/izyan/app
RUN mkdir -p /home/izyan/staticfiles
RUN mkdir -p /home/izyan/media
RUN addgroup -S izyan && adduser -S izyan -G izyan
RUN chown -R izyan:izyan /home/izyan
# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

USER izyan

WORKDIR /home/izyan/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt app ./
COPY bin/wait-for $HOME/bin/wait-for

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
