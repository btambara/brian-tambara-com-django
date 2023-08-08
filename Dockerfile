FROM python:3.11

WORKDIR /app

COPY brian_tambara_com .

COPY setup/requirements.txt requirements.txt

RUN pip install -r requirements.txt
