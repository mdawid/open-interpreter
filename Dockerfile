FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade && apt-get -y install sudo

RUN pip install --upgrade pip && pip install --no-cache-dir poetry==1.6.1

RUN pip install numpy pandas matplotlib requests beautifulsoup4

WORKDIR /app

COPY . /app

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

ENTRYPOINT ["poetry", "run", "interpreter"]
CMD []