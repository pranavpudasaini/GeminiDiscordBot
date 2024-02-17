FROM alpine:3.14

WORKDIR /app

COPY ./ ./
RUN apk add --no-cache jq curl python3 bash py3-pip gcc python3-dev libc-dev
RUN pip install -U -r requirements.txt

CMD ["python3", "gembot.py"]
