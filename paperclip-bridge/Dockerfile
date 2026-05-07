FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bridge.py .
COPY config.yaml .
COPY skill-role-map.yaml .

CMD ["python", "bridge.py"]
