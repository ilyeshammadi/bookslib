# Books Library


A platform to read and share books with other users, the platform tracks users activity on the platform. The collected data is exposed as a GraphQL API for future application like integrating a recommendation engine.


.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT

## Settings
Clone the project locally
```shell
$ git clone https://github.com/Ilyes-Hammadi/bookslib
$ cd bookslib
```

Install all the required packages
```shell
$ pip install -r requirements/base.txt
```

Create a Postgres database named `books_library` with the default postgres user and password
```shell
$ createdb books_library
```

Export the DJANGO_URL project env variable to link the database with the django settings
```shell
$ source local-env.sh
```

Migarte all the model
```shell
$ python manage.py migrate
```

Create a superuser
```shell
$ python manage.py createsuperuser
```

## Deployment
The following details how to deploy this application.


### Heroku
See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html



### Docker

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html


