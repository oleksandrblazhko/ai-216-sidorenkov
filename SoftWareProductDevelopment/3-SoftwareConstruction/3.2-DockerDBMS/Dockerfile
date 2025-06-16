FROM python:3.11

RUN pip install psycopg2-binary

COPY client_postgres.py /app/
WORKDIR /app

CMD ["python", "client_postgres.py"]
