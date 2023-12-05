FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY main.py requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
