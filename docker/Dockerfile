FROM python:3.12-slim-bookworm AS python-base

WORKDIR /var/www/datax

FROM python-base AS python-virtualenv

RUN python -m pip install virtualenv
RUN python -m virtualenv .venv

RUN . .venv/bin/activate && python -m pip install pip-tools

FROM python-virtualenv AS python-modules

COPY requirements.in .
COPY dev-requirements.in .

RUN . .venv/bin/activate && python -m piptools compile requirements.in
RUN . .venv/bin/activate && python -m piptools compile dev-requirements.in

RUN . .venv/bin/activate && python -m piptools sync requirements.txt dev-requirements.txt

FROM python-modules AS final

COPY ./docker/docker-entrypoint.sh .

EXPOSE 8000
ENTRYPOINT ["/var/www/datax/docker-entrypoint.sh"]