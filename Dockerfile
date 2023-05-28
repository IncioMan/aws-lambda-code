FROM python:3.10-slim

WORKDIR /code

RUN pip install pipenv

CMD ["tail", "-f", "/dev/null"]