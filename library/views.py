from django.shortcuts import render, get_object_or_404
from .models import Book, Category

def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'library/book_list.html', {
        'books': books,
        'categories': categories
    })

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'library/book_detail.html', {'book': book})