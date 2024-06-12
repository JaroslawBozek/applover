FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./app /app
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN apt-get update && apt-get install -y sqlite3

ENV PYTHONPATH /app

EXPOSE 3000
CMD ["python", "main.py"]
