# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import re

from init_data.base import get_books
from books_library.users.models import User


books = get_books()

print('Start inserting users...')

counter = 0

for index, book in books.iterrows():
    author = book['Book-Author']
    username = book['Book-Author'].split(' ')[0]
    username = re.sub('[!@#$.,;:]', '', username)

    if not User.objects.filter(username=username).exists():
        u = User.objects.create_user(username=username, password='bookslib123')
        u.save()
        counter += 5
    
    if counter > 100:
        break


print('Finished inserting users')
