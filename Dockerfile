FROM zalando/ubuntu:15.04-1

MAINTAINER Chris Viola

RUN apt-get update && apt-get clean &&  \
    apt-get install -y unattended-upgrades && \
    apt-get install -y tar git curl nano wget dialog net-tools build-essential && \
    apt-get install -y python3-pip

RUN pip3 install --upgrade stups-tokens stups

ADD app/ /opt/app

CMD python3 /opt/app/tokeninfo.py
