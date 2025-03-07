FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY mqtt_listener.py /app/
COPY data_processor.py /app/
COPY database.py /app/

CMD [ "python", "/app/mqtt_listener.py" ]
