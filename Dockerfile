FROM python:3.11-alpine

WORKDIR /root/equator/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "./equator/manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python", "./equator/manage.py", "runserver_plus", "--cert-file", "cert.pem", "--key-file", "key.pem"]
