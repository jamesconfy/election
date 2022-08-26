FROM python:3.10.2-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

ENV PORT=80

EXPOSE 80

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 run:app