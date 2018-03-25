FROM ubuntu:latest
MAINTAINER sih4sing5hong5

RUN apt-get update -qq
RUN apt-get install -y python3 g++ python3-dev
RUN sudo apt-get install -y libav-tools


# Switch locale
RUN locale-gen zh_TW.UTF-8
ENV LC_ALL zh_TW.UTF-8

RUN pip install --upgrade tai5-uan5_gian5-gi2_hok8-bu7 django line-bot-sdk

COPY . .
RUN python manage.py migrate
