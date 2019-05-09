from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

#Defining the admin class 
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book','id','imprint','status', 'due_back')
	list_filter = ('book','imprint','status', 'due_back')


