#!/bin/sh
export FLASK_APP=server.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run --host=localhost --port=6006
