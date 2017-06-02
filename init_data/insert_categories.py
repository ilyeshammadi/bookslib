from django.core.files import File

from books_library.books.models import Category

print('Start inserting categories...')

# Fiction
c = Category(name='Fiction', image=File(open('init_data/categories_images/f.jpg')))
c.save()


# Science Fiction
c = Category(name='Science Fiction', image=File(open('init_data/categories_images/sf.jpg')))
c.save()


# Programming
c = Category(name='Programming', image=File(open('init_data/categories_images/pr.jpg')))
c.save()


# Mathematics
c = Category(name='Mathematics', image=File(open('init_data/categories_images/m.jpg')))
c.save()

# Physics
c = Category(name='Physics', image=File(open('init_data/categories_images/p.jpg')))
c.save()

print('Finished inserting categories...')
