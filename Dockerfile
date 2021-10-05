FROM python:3.8.3-slim-buster
ENV PYTHONBUFFERED=1
WORKDIR /groceryapi
COPY requirements.txt /groceryapi/
RUN pip install -r requirements.txt
COPY . /groceryapi/