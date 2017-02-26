from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView, UpdateView, DetailView

from .forms import BookForm
from .models import Book, Category


def index(request, category_slug=None):
    # Get all the books
    books = Book.objects.all()

    # Get all the categories
    categories = Category.objects.all()

    # Init the search terms
    search = None

    # If request is post
    if request.method == 'POST':
        search = request.POST.get('search')

    # Category filter
    if category_slug:
        books = books.filter(categories__slug=category_slug)

    # Search filter
    if search:
        # Split the search into terms
        terms = search.split(',')

        # Decalre an empty query
        q = Q()

        # Go through each term
        for term in terms:
            q |= Q(name__contains=term)
            q |= Q(author__contains=term)
            q |= Q(tags__name__contains=term)

        books = books.filter(q).distinct()

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
        'books': books,
        'categories': categories,
        'category_slug': category_slug
    }
    return render(request, 'books/index.html', context)


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
