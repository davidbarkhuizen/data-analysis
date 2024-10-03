FROM python:3.12-slim-bookworm AS python-base

WORKDIR /var/www/data

FROM python-base AS python-virtualenv

RUN python -m pip install virtualenv
RUN python -m virtualenv .venv
RUN . .venv/bin/activate && python -m pip install pip-tools

FROM python-virtualenv AS python-modules

COPY requirements.in .
RUN . .venv/bin/activate && python -m piptools compile
RUN . .venv/bin/activate && python -m piptools sync

FROM python-modules AS final
