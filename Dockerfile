FROM python:3.10

WORKDIR /code

RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root
