FROM python:3.9.22-alpine3.21

WORKDIR /app

COPY Backend/app.py /app

RUN pip install flask

EXPOSE 5000

CMD ["python3", "app.py"]

