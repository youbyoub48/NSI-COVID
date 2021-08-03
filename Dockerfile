FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install python3 python3-pip -y\
    && pip install --upgrade pip

ADD . /app/
WORKDIR /app

RUN pip install -r requirements.txt \
    && python3 src/manage.py collectstatic

EXPOSE 8000
CMD [ "python3", "src/manage.py", "runserver" , "0.0.0.0:8000"]