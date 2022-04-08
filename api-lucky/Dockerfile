FROM python:3-alpine3.15

WORKDIR /app

# Copy the requirements.txt file for dependencies
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the .py files and config.json
COPY config.json config.json
COPY *.py .

CMD [ "python3", "/app/app.py"]

