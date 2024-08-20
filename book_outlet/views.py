from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("title")
    total_of_books = books.count()
    rating_average = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html",{
        'books': books,
        'total_of_books': total_of_books,
        'rating_average': rating_average,
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html",{
        "book": book,
    })