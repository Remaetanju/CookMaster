# syntax=docker/dockerfile:1
FROM python:3.10.13-alpine3.18

WORKDIR src/

#RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pwd
RUN cat requirements.txt

COPY ./src/ .
CMD ["python", "main.py"]
