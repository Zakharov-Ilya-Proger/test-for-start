FROM python:3.12-alpine

WORKDIR /app

COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
