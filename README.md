[![Actions Status](https://github.com/DzmitrySha/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/DzmitrySha/python-project-52/actions)
[![workflow](https://github.com/DzmitrySha/python-project-52/actions/workflows/django_ci.yml/badge.svg)](https://github.com/DzmitrySha/python-project-52/actions/workflows/django_ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/26d9c4b106cb33a348a0/maintainability)](https://codeclimate.com/github/DzmitrySha/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/26d9c4b106cb33a348a0/test_coverage)](https://codeclimate.com/github/DzmitrySha/python-project-52/test_coverage)

# Task Manager

_Register, create, delete and edit tasks, labels and statuses, assign executors to tasks. Filter tasks by tags, statuses, and executors, or filter only your created tasks._

##  DEMO

Just click and try to use **[DEMO on Railway](https://python-project-52-production-af44.up.railway.app/)** or 
**[DEMO on REG.RU](http://project52.site/)**

_P.S.: You will need to register to try all the features in demo._

## Installation

Clone the repository:

`git clone https://github.com/DzmitrySha/python-project-52.git`

Go to the project folder:

`cd python-project-52`

Install dependencies with Poetry:

(If you don't have Poetry, follow this guide to install it: [Install Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer))

`make install`

## Settings

Create an .env file: 

`touch .env`

Write following constants to the .env file:

`SECRET_KEY=your_Django_secret_key` (generate one with `make secretkey` command)

`DATABASE_URL=your_database_url_path` (to use simple sqlite database use this path: `DATABASE_URL='sqlite:///db.sqlite3'`)

## Database preparation

`make migrations`

`make migrate`

`make createsuperuser`

## Start project

`make runserver`

Use this app in browser on http://localhost:8080

---
Good Luck!

