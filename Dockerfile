# To implement
# Using Alpine version because it's lightweight
FROM python:3.8-alpine
WORKDIR /app

COPY . .

RUN apk update && apk upgrade && \
    pip install --no-cache-dir pipenv && \
    pipenv install --ignore-pipfile && \
    apk del py3-pip py-pip && \
    rm -rf /root/.cache/pip && \
    rm -f /sbin/apk && \
    rm -rf /etc/apk && \
    rm -rf /lib/apk && \
    rm -rf /usr/share/apk && \
    rm -rf /var/lib/apk

CMD ["pipenv", "run", "start"]
