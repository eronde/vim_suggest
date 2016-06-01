FROM ubuntu:14.04.3

RUN apt-get update && apt-get install -yq python3-dev python3-pip

ADD . /code
WORKDIR /code

RUN pip3 install  -r requirements.txt

