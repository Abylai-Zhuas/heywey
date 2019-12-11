from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import CreateView
from .forms import *


def index(request):
	latest_books_list = Book.objects.order_by('-pub_date')[:5]
	popular_books = Book.objects.filter(numberOfClicks__gt = 3).order_by('-numberOfClicks')[:3]
	return render(request, 'books/index.html', {'latest_books_list' : latest_books_list,
												'popular_books' : popular_books})

def book(request, book_id):
	art = get_object_or_404(Book, pk = book_id)
	art.numberOfClicks += 1
	art.save()
	comment = showComments(request, book_id)

	if request.method == "POST":
		try:
			txt = request.POST.get('comment_text')
			print(request.POST)
			comment	= Comments(comment_text = txt,
								book = Book.objects.get(pk = book_id), user = SimpleUser.objects.get(username = request.POST['username']))
			comment.save()
		except:
			print('The comment can\'t be added')
	return render(request, "books/book.html", {"book": art, "comment" : comment})

def search(request):
    try:
        if request.method=="POST":
            text_for_search = request.POST.get("search_field")
            if len(text_for_search)>0:
                search_res = Book.objects.filter(description__contains=text_for_search)
            return render(request, "search.html",
                        {"search_res":search_res,"empty_res":"There is no product"})
    except:
        return render(request, "search.html",{"empty_res":"There is no product"})
 
def archive(request):
    context = Book.objects.all()
    return render(request, "books/archive.html", {"context":context})

def addComment(request, book_id):
    try:
        txt = request.POST.get("comment_text")
        comment = Comments(comment_text = txt,
                            book = Book.objects.get(pk = book_id))
        comment.save()
        return render(request, "books/book.html",
                                {"book":Book.objects.get(pk = book_id)})
    except:
        return HttpResponse("No such books")

def showComments(request, book_id):
    try:
        comments = Comments.objects.filter(book = Book.objects.get(pk = book_id))
        return comments
    except:
        return "No comments yet"

def profile(request):
    return render(request, "books/user_page.html")

class registerView(CreateView):
    form_class = SimpleUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def contacts(request):
    return render(request, "books/contacts.html")