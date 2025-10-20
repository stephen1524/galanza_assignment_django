from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category
from .forms import CommentForm

def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'library/book_list.html', {
        'books': books,
        'categories': categories
    })

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    comments = book.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('book_detail', id=book.id)
    else:
        form = CommentForm()

    return render(request, 'library/book_detail.html', {
        'book': book,
        'comments': comments,
        'form': form
    })