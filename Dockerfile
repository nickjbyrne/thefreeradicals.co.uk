FROM python:3.6.5-alpine
MAINTAINER Nick Byrne <nick@incension.com>

ARG port
ARG addr
ENV PORT=$port
ENV ADDR=$addr

RUN apk add --update make

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN make publish

EXPOSE $PORT

CMD ["sh", "entrypoint.sh"]
