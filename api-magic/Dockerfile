FROM python:slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
# Install dependencies
RUN pip3 install -r requirements.txt

COPY app.py app.py

CMD [ "python3", "/app/app.py"]

