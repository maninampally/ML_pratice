FROM python:3.13.9-slim
WORKDIR /app
COPY . /app

RUN apt-get update -y && apt install awscli -y

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
