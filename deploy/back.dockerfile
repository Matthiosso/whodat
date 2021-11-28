FROM python:3.9-alpine

ENV PIP_DISABLE_PIP_VERSION_CHECK="1"

RUN apk add build-base


RUN apk add --no-cache supervisor postgresql-dev \
    && python -m pip install --upgrade pip

WORKDIR /app

COPY back/requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
  pip install -r requirements.txt

COPY back/*.py .

ENV FLASK_APP=./app.py
ENV FLASK_ENV=development

CMD [ "flask", "run", "--host", "0.0.0.0" ]
