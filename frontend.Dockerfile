FROM python:3.9.22-alpine3.21

WORKDIR /app

COPY Frontend/. /app

RUN pip install flask && pip install requests

EXPOSE 8080

CMD ["python3", "front.py"]

