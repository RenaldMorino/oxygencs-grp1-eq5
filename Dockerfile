## To implement
## Using Alpine version because it's lightweight
FROM python:3.8-alpine
WORKDIR /app
COPY . .

RUN apk update && apk upgrade && \
    pip install pipenv && \
    pipenv install --ignore-pipfile

CMD ["pipenv", "run", "start"]
