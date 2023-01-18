#!/bin/bash
ls

echo $BACKEND_CORS_ORIGINS
echo "Run migrations"
alembic upgrade head

# echo "Create initial data in DB"
# python -m app.initial_data
