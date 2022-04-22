FROM python:slim-buster
WORKDIR /app

COPY api-magic/requirements.txt requirements.txt
# Install dependencies
RUN pip3 install -r requirements.txt

COPY api-magic/app.py app.py

CMD [ "python3", "/app/app.py"]

