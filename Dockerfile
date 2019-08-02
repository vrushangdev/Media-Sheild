FROM python:3.7-alpine
MAINTAINER Vrushang Desai
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir /app
WORKDIR /app
COPY ./MediaApi /app

RUN adduser -D user
USER user