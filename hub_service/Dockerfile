FROM python:3.7

RUN pip install Django requests

COPY . /app/

WORKDIR /app/

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]