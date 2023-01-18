export $(grep -v '^#' env/.env | xargs)
poetry run alembic revision --autogenerate -m "init time test model"