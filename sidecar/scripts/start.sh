#! /usr/bin/env sh
set -e

if [ -f /app/app/main.py ]; then
    DEFAULT_MODULE_NAME=app.main
fi

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
MODULE_NAME=${MODULE_NAME:?"No module name provided"}
VARIABLE_NAME=${VARIABLE_NAME:-app}

export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

if [ -f /app/app/gunicorn_conf.py ]; then
    DEFAULT_GUNICORN_CONF=/app/app/gunicorn_conf.py
fi

GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}
GUNICORN_CONF=${GUNICORN_CONF:?"No module name provided"}

export WORKER_CLASS=${WORKER_CLASS:-"uvicorn.workers.UvicornWorker"}

# If there's a prestart.sh script in the /app/app directory
# or other path specified, run it before starting
sh scripts/init.sh

PRE_START_PATH=${PRE_START_PATH:-/app/scripts/prestart.sh}
echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else 
    echo "There is no script $PRE_START_PATH"
fi

# Start Gunicorn
exec gunicorn -k "$WORKER_CLASS" -c "$GUNICORN_CONF" "$APP_MODULE"