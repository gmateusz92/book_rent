from django.shortcuts import render
from .models import BookTitle
# Create your views here.

def book_title_list_view(request):
    qs = BookTitle.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'books/main.html', context)

def book_title_detail_view(request, pk):
    obj = BookTitle.objects.get(pk=pk)
    context = {
        'obj': obj
    }
    return render(request, 'books/detail.html', context)