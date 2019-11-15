from django.shortcuts import render
from . models import Book, Comment

def index(request):
	latest_books_list = Book.objects.order_by('-pub_date')[:5]
	return render(request, 'books/list.html', {'latest_books_list' : latest_books_list})