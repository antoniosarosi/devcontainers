FROM python:3.10-slim AS base
WORKDIR /code
RUN apt-get update && apt-get install -y default-libmysqlclient-dev
RUN pip install pipenv

FROM base AS builder
ENV PIPENV_VENV_IN_PROJECT=1
RUN apt-get install -y build-essential

FROM builder AS installer
COPY Pipfile Pipfile.lock ./
RUN pipenv install

FROM base AS runner
COPY --from=installer /code/.venv /code/.venv
COPY . /code
CMD pipenv run gunicorn --bind 0.0.0.0:5000 src.app:app 
