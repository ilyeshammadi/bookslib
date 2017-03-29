from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DetailView


from .forms import BookForm
from .models import Book, Category

from ..navigation.models import Search, BookHistory

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

        # If the search has results, save the searched terms
        if len(books) > 0:
            search_history = Search()
            search_history.terms = search
            search_history.user = request.user
            search_history.save()


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
    def get_object(self):
        """Return the requested book and save the navigation"""
        # Get the object from the super class method
        book = super(BookDetailView, self).get_object()

        # If the user is logged in, save the book history actions
        if self.request.user.is_authenticated():

            # Get the logged in user
            user = self.request.user

            # Test if the user is viewing the book
            # for the first time
            try:
                book_history = BookHistory.objects.get(book=book, user=user)
            except:
                book_history = BookHistory(book=book, user=user, viewed=True)
                book_history.save()

        return book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm

@login_required
def book_read(request, id):
    """Returns the book link pdf"""
    # Get the logged in user
    user = request.user

    # Get the Book to read
    book = get_object_or_404(Book, pk=id)

    # Get the Book history
    book_history = get_object_or_404(BookHistory, book=book, user=user)
    book_history.read = True
    book_history.save()

    # Return the PDF link
    return redirect(book.link_to_pdf)

