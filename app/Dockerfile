FROM python:3.6-stretch

RUN adduser --system --group --no-create-home app

COPY . /app

WORKDIR /app

RUN pip install requests

RUN pip install -r requirements.txt

RUN chown -R app:app /app

USER app