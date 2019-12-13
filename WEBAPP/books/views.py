from django.http import HttpResponse, Http404, HttpResponseRedirect, FileResponse
from .models import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import CreateView
from .forms import *
from django.utils.text import slugify



def index(request):
	latest_books_list = Book.objects.order_by('-pub_date')[:5]
	popular_books = Book.objects.filter(numberOfClicks__gt = 8).order_by('-numberOfClicks')[:4]
	return render(request, 'books/index.html', {'latest_books_list' : latest_books_list,
												'popular_books' : popular_books})

def book(request, book_id):
	art = get_object_or_404(Book, pk = book_id)
	art.numberOfClicks += 1
	art.save()
	comments = showComments(request, book_id)

	if request.method == "POST":
		try:
			txt = request.POST.get('comments_text')
			print(request.POST)
			comment	= Comments(comments_text = txt,
								book = Book.objects.get(pk = book_id), user = SimpleUser.objects.get(username = request.POST['username']))
			comment.save()
		except:
			print('The comment can\'t be added')
	return render(request, "books/book.html", {"book": art, "comments" : comments})

def search(request):
    try:
        if request.method=="POST":
            book_title = request.POST.get("search_field")
            if len(book_title)>0:
                search_res = Book.objects.filter(book_title__contains = book_title)
            return render(request, "books/search.html",
                        {"search_res":search_res,"empty_res":"There is no product"})
    except:
        return render(request, "books/search.html",{"empty_res":"There is no product"})
<<<<<<< HEAD

=======
 
>>>>>>> 6e16ce6f8027f9fdd4fbf376e69b295fa5b9d8b1
def archive(request):
    context = Book.objects.all()
    return render(request, "books/archive.html", {"context":context})

def addComment(request, book_id):
    try:
        txt = request.POST.get("comments_text")
        comment = Comments(comments_text = txt,
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

def download(request, book_id):
    item = get_object_or_404(book_content, pk=book_id)
    file_name, file_extension = os.path.splitext(item.file.file.name)
    file_extension = file_extension[1:] # removes dot
    response = FileResponse(item.file.file, 
        content_type = "file/%s" % file_extension)
    response["Content-Disposition"] = "attachment;"\
        "filename=%s.%s" %(slugify(item.file.name)[:100], file_extension)
    return response