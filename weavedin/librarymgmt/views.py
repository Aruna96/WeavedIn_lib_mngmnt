from django.shortcuts import render, redirect

from .models import Book
from .models import Author

# Create your views here.


def addAuthor(request):
	if request.method == 'POST':
		print request.POST
		author = Author()
		author.author_name = request.POST.get('name')
		author.age  = request.POST.get('age')
		author.gender = request.POST.get('gender')
		author.born = request.POST.get('born')
		author.abtauthor = request.POST.get('abot')
		author.save()
		return redirect('/authors')
		# return render(request, 'addauthornew.html')
		
	return render(request, 'addauthornew.html')

def see_author(request):
	details = Author.objects.values()
	return render(request, "authors.html", { 'details': details })

def listAuthors(request):
	authors = Author.objects.values()
	print authors
	return render(request, 'authors.html', {'authors': authors})

def addBook(request):
	if request.method == 'POST':
		print request.POST
		book = Book()
		book.book_name = request.POST.get('bname')
		book.isbn  = request.POST.get('num')
		book.desc = request.POST.get('abt')
		book.author = request.POST.get('author')
		book.save()
		return redirect('/books')#save
		
	data = Author.objects.values()
	return render(request, 'addbookn.html', {'details' : data})
	

def listBooks(request):
	books = Book.objects.values()
	print books
	return render(request, 'books.html', {'books': books})