MANAGE := poetry run python manage.py
HEROKU := heroku run python manage.py

install:
		poetry install

runserver:
		$(MANAGE) runserver 8080

shell:
		$(MANAGE) shell_plus

collectstatic:
		$(MANAGE) collectstatic

messages:
		poetry run django-admin makemessages -l ru

compilemess:
		poetry run django-admin compilemessages

migrations:
		$(MANAGE) makemigrations

migrate:
		$(MANAGE) migrate

migrations-h:
		$(HEROKU) makemigrations

migrate-h:
		$(HEROKU) migrate

makesecretkey:
		poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'

run-gunicorn:
		export DJANGO_SETTINGS_MODULE=task_manager.settings
		poetry run gunicorn task_manager.wsgi --log-file -

selfcheck:
		poetry check

test:
		poetry run pytest

test-cov:
		poetry run pytest --cov

test-django:
		python manage.py test

lint:
		poetry run flake8 task_manager

test-coverage:
		poetry run pytest --cov=task_manager --cov-report xml

check: selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build shell migrate collectstatic