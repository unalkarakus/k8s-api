FROM python:3-alpine

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy the requirements.txt file for dependencies
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the .py files and config.json
COPY config.json config.json
COPY *.py .

RUN touch current.txt
RUN chown -R appuser:appgroup /app
RUN chmod 777 /app
RUN chmod 777 current.txt

USER appuser
CMD [ "python3", "/app/app.py"]

