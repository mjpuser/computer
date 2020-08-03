FROM python:alpine

RUN apk add g++
RUN pip install 'aiormq>=3.2.3,<4' 'redis>=3.5,<4'

ENTRYPOINT ["python", "main.py"]
