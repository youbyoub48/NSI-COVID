FROM python:3.8-slim

ADD . /app/
WORKDIR /app

RUN pip install -r requirements.txt \
    && python3 src/manage.py collectstatic

EXPOSE 8000
CMD [ "python3", "src/manage.py", "runserver" , "0.0.0.0:8000"]