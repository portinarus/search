FROM python:3.6-alpine

RUN mkdir -p /home/search
WORKDIR /home/search
ADD . /home/search

RUN apk update && \
    apk add --no-cache make curl autoconf automake make g++ && \
    apk add --no-cache wget supervisor postgresql-dev
RUN pip install -r requirements.txt
