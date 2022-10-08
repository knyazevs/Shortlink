FROM python:3.9.14-alpine3.16

WORKDIR /home/shortlink

RUN apk add postgresql-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]
