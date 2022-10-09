install:
		poetry install

package-install:
		python3 -m pip install --user dist/*.whl

package-uninstall:
		python3 -m pip uninstall --yes dist/*.whl

runserver:
		poetry run python manage.py runserver

run-gunicorn:
		export DJANGO_SETTINGS_MODULE=task_manager.settings
		poetry run gunicorn task_manager.wsgi

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

.PHONY: install test lint selfcheck check build