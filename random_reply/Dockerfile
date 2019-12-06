FROM python:3.7

RUN pip install Django

COPY . /app/

WORKDIR /app/

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]