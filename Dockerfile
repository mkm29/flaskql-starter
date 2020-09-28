FROM python:3.6.0-alpine
LABEL name="Flask + GraphQL Starter App" maintainer="Mitchell Murphy<mitch.murphy@gmail.com>"
# set work directory
WORKDIR /usr/src/app
USER root
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile* ./
RUN apk --update add libffi-dev py-pip nano \
    && apk add postgresql-dev gcc python3-dev musl-dev && \
    pip install pipenv && \
    pipenv install --system --deploy
COPY . .
USER 1001
EXPOSE 8080
CMD gunicorn --bind 0.0.0.0:8080 wsgi
