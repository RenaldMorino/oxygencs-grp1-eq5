## To implement
## Using Alpine version because it's lightweight
FROM python:3.8-alpine
WORKDIR /app

RUN apk update && apk upgrade && \
    pip install pipenv && \
    pipenv install --ignore-pipfile

COPY . .

CMD ["pipenv", "run", "start"]
