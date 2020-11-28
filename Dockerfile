FROM python:slim

RUN mkdir /app

WORKDIR /app

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
