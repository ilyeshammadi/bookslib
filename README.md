# Books Library


A platform to read and share books with other users, the platform tracks users activity on the platform. The collected data is exposed as a GraphQL API for future application like integrating a recommendation engine.

This project is part of my Bachelor thesis and the complete thesis can be found a this [link](https://www.slideshare.net/slideshow/embed_code/key/vTsPgSstHm3oI3).

## Screenshots
### Home
![](https://github.com/Ilyes-Hammadi/bookslib/blob/master/docs/img/platform.png)
### Book Detail 
![](https://github.com/Ilyes-Hammadi/bookslib/blob/master/docs/img/book_detail.png)
### User profile
![](https://github.com/Ilyes-Hammadi/bookslib/blob/master/docs/img/user_follow.png)


## Features
This are the most important features in the platform:
- Users can join the platform to read books
- Social Authentification
- User can follow each other
- Include two types of APIs (GraphQL, DRF)
- Collected user data from the platform and there twitter account
- Can plugin recommendation engine

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

### Fake Data
You can insert thousands of data collected from the [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)
```shell
$ python insert.py
```

## Acces the API
This project include two kind of APIs:
- GraphQL API ==> `/graphql`
- Django Rest Framework API ==> `/api`

The GraphQL API is used to expose the collected data so that they can consumed by the recommedation engine.

The DRF API is consumed by frontend appilications (AJAX, Android), it includes JWT for remote authentification.


## Deployment
The following details how to deploy this application.


### Heroku
See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html)



### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html)


## License
[MIT](https://github.com/Ilyes-Hammadi/bookslib/blob/master/LICENSE)
