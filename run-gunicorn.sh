#!/usr/bin/env bash
gunicorn password123:app --log-level info -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000