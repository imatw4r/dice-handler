FROM python:3.8-alpine

RUN mkdir /app
WORKDIR /app


COPY requirements.txt .

RUN pip --disable-pip-version-check install -r requirements.txt

COPY . .

EXPOSE 80

RUN python manage.py makemigrations
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:80
