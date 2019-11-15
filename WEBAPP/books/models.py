import datetime
from django.db import models
from django.utils import timezone

class Book(models.Model):
    book_title = models.TextField('Name of the book')
    book_text = models.TextField('Text of the book')
    pub_date = models.DateTimeField('Date of publication')

    def __str__(self):
    	return self.book_title

    def was_published_recently(self):
   		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    author_name = models.TextField('Name of author')
    comment_text = models.TextField('Text of comment')

    def __str__(self):
    	return self.author_name