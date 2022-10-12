MANAGE := poetry run python manage.py
HEROKU := heroku run python manage.py

install:
		poetry install

package-install:
		python3 -m pip install --user dist/*.whl

package-uninstall:
		python3 -m pip uninstall --yes dist/*.whl

runserver:
		$(MANAGE) runserver

shell:
		$(MANAGE) shell_plus

collectstatic:
		$(MANAGE) collectstatic

migrations:
		$(MANAGE) makemigrations

migrate:
		$(MANAGE) migrate

migrations-heroku:
		$(HEROKU) makemigrations

migrate-heroku:
		$(HEROKU) migrate

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
		poetry run pytest --cov=task_manager --cov-report xml tests/

check: selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build shell migrate collectstatic