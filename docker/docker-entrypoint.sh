#!/usr/bin/env bash

. .venv/bin/activate && cd src && python -m uvicorn --reload --port 8000 --host 0.0.0.0 server.app:app