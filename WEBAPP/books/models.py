from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings

class Editor(models.Model):
    editor_name = models.CharField(max_length = 100)
    editor_surname = models.CharField(max_length = 100)

    def __str__(self):
        return self.editor_name + " " + self.editor_surname

class Book(models.Model):
    book_title = models.TextField(default = "")
    book_author = models.TextField('Name of author of the book')
    book_text = models.TextField('Text of the book')
    pub_date = models.DateTimeField('Date of publication')
    rating = models.FloatField(default = 0.0)
    editor_id = models.ForeignKey(Editor, on_delete = models.CASCADE)
    book_genre = models.TextField('Genre of book')
    numberOfClicks = models.IntegerField(default = 0)
    book_image = models.ImageField(upload_to = 'archive', default = 'NULL')
    book_content = models.FileField(upload_to = 'media', default = 'NULL')

    def __str__(self):
    	return self.book_title

    def rate_book(self, new_rate):
        if self.rating == 0.0:
            self.rating = new_rate
            return self.rating
        else:
            return (self.rating + new_rate)/2

    def was_published_recently(self):
   		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

class SimpleUser(AbstractUser):
    userImg = models.ImageField(upload_to = 'user_avas/', default = 'NULL')

    def __str__(self):
        return self.username

class Comments(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    comments_text = models.TextField('Text of comment')

    def __str__(self):
    	return self.comment_text

class Ads(models.Model):
    ads_owner = models.CharField(max_length = 100)
    ads_content = models.TextField()
    file = models.FileField(upload_to = "notebooks", default = "NULL")

    def __str__(self):
        return self.ads_content