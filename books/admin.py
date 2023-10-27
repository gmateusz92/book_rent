from django.contrib import admin
from .models import Book, BookTitle

admin.site.register(BookTitle)
admin.site.register(Book)
# Register your models here.
