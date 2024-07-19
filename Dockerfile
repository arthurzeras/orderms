FROM python:3.10 AS base

WORKDIR /code

RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

FROM base AS api
CMD ["sh", "./start.sh"]

FROM base AS consumer
CMD ["python", "manage.py", "launch_consumer"]