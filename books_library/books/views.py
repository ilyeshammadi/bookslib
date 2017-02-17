
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView, UpdateView, DetailView

from .forms import BookForm
from .models import Book

# TODO: Add search feature here
def index(request):
    books = Book.objects.all()
    paginator = Paginator(books, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)

    return render(request, 'books/index.html', {'books': books})


class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
