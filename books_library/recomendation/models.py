from __future__ import unicode_literals

import json

from django.db import models

import requests


# Create your models here.
class Recommender(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=120, default='my-recommender', unique=True)

    def __str__(self):
        return '{0} - {1}'.format(self.id, self.url)

    def similar_books(self, book_id):
        content = requests.get(self.url + str(book_id)).content

        print(self.url + str(book_id))

        return json.loads(content)

