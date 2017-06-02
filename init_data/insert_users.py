# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import re

from init_data.base import get_books
from books_library.users.models import User

print('Start inserting users...')

books = get_books()


counter = 0

for _, book in books.iterrows():
    author = book['Book-Author']


    username = book['Book-Author'].split(' ')[0]
    username = re.sub('[!@#$.,;:]', '', username)

    # If username is not taken
    if not User.objects.filter(username=username).exists():
        u = User.objects.create_user(username=username, password='bookslib123')
        u.save()
        counter += 1


    if counter > 230:
        break

print('Finished inserting users...')
