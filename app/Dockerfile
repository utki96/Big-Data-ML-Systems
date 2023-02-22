FROM python:3.9-slim-buster

WORKDIR /app

ENV OTEL_EXPORTER_JAEGER_ENDPOINT http://jaeger:14268/api/traces
ENV OTEL_RESOURCE_ATTRIBUTES service.name=my-hello-service

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

