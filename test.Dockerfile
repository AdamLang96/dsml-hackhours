FROM python:3.8-slim-buster

WORKDIR /build

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV solutions_env = TRUE

ENTRYPOINT ["pytest", "tests"]

