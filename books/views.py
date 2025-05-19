from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all().order_by('title')

    # Get search query
    query = request.GET.get('q')
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    # Get items per page from dropdown
    per_page = request.GET.get('per_page', 5)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 5 # Default to 5 if per_page is not a valid integer

    paginator = Paginator(books, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'page_obj': page_obj, 'per_page': per_page, 'query': query})
