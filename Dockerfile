FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y gettext

RUN python manage.py collectstatic
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py compilemessages

EXPOSE 8000
