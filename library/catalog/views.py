from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre, Language
# Create your views here.

def index(request):
	#HomePage
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.all().count()
	num_visits = request.session.get('num_visits',0)
	request.session['num_visits'] = num_visits + 1
	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
		'num_visits': num_visits,
	}

	return render(request, 'index.html', context=context)

from django.views import generic

from django.contrib.auth.decorators import login_required

@login_required
def BookList(request):
	booklist = Book.objects.all()
	context = {
	'book_list': booklist,
	}
	return render(request, 'catalog/book_list.html', context=context)


#class BookListView(generic.ListView):
#	model = Book

class BookDetailView(generic.DetailView):
	model = Book

class AuthorListView(generic.ListView):
	model = Author

class AuthorDetailView(generic.DetailView):
	model = Author
