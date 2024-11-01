FROM python:3.12

RUN pip install poetry

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY . .

EXPOSE 8000

RUN poetry install

CMD python manage.py runserver 0.0.0.0:8000