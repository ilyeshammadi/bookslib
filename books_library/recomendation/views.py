import json
import random
import requests

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from taggit.models import Tag

from books_library.books.models import Book, Category
from books_library.navigation.models import BookHistory
from books_library.recomendation.models import Recommender


@login_required
def suggestion(request):
    """ Suggest books according to the logged in user profile data"""
    books = Book.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    user = request.user

    # Show 25 contacts per page
    paginator = Paginator(books, 25)

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)

    context = {
        "books": books,
        'categories' : categories,
        'tags' : tags
    }
    return render(request, 'recomendation/suggestion.html', context)


def get_rec(book_id):
    rec = Recommender.objects.get(name='my-recommender')
    return rec.similar_books(book_id=book_id)['payload']
