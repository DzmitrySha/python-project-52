LOCAL := poetry run python manage.py
HEROKU := heroku run python manage.py
RAILWAY := railway run python manage.py

install:
		poetry install

# runserver commands
runserver:
		$(LOCAL) runserver 8080
run-gunicorn:
		export DJANGO_SETTINGS_MODULE=task_manager.settings
		poetry run gunicorn task_manager.wsgi --log-file -

# service commands
shell:
		$(LOCAL) shell_plus
collectstatic:
		$(LOCAL) collectstatic
makesecretkey:
		poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'

# make translate messages commands
messages:
		poetry run django-admin makemessages -l ru
compilemess:
		poetry run django-admin compilemessages

# migrate commands
migrations:
		$(LOCAL) makemigrations
migrate:
		$(LOCAL) migrate
migrations-hr:
		$(HEROKU) makemigrations
migrate-hr:
		$(HEROKU) migrate
migrations-rw:
		$(RAILWAY) makemigrations
migrate-rw:
		$(RAILWAY) migrate

# test commands
test:
		poetry run pytest
test-cov:
		poetry run pytest --cov
test-django:
		$(LOCAL) test
test-coverage:
		poetry run pytest --cov=task_manager --cov-report xml

# linter & check commands
lint:
		poetry run flake8 task_manager
selfcheck:
		poetry check

# complex commands
check: selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build shell migrate collectstatic