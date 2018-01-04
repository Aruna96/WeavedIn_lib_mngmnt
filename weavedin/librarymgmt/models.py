from django.db import models

# Create your models here.


class Book(models.Model):
	# book_id = models.AutoField(primary_key=True)
	book_name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	isbn = models.CharField(max_length=100)
	desc = models.CharField(max_length=200)

class Author(models.Model):
	author_id = models.AutoField(primary_key=True)
	author_name = models.CharField(max_length=100)
	age = models.IntegerField()
	gender = models.CharField(max_length=6)
	born = models.CharField(max_length=50)
	abtauthor = models.CharField(max_length=100)
		