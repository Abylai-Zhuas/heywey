from django.urls import path
from django.contrib.auth.views import auth_login
from . import views

app_name = 'books'

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('book/<int:book_id>/', views.book, name = 'book'),
    path('search/', views.search, name = 'search'),
    path('archive/', views.archive, name = 'archive'),
    path('book/<int:book_id>/comment', views.addComment, name = 'addComment'),
    path('contacts/', views.contacts, name = "contacts"),
    path('', auth_login, name = "login"),
    path("register", views.registerView.as_view(), name = "registration"),
    path("user/", views.profile, name = "profile"),
    path('' , views.download, name = "download"),
]