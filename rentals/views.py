from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .forms import SearchBookForm
from books.models import Book
from django.views.generic import ListView, UpdateView, CreateView, FormView
from .models import Rental
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

def search_book_view(request):
    form = SearchBookForm(request.POST or None)
    search_query = request.POST.get('search', None)
    book_ex = Book.objects.filter(Q(isbn=search_query) | Q(id=search_query)).exists()

    if search_query is not None and book_ex:
        return redirect('rentals:detail', search_query)
        

    context = {
         'form': form,
    }
    return render(request, 'rentals/main.html', context)

class BookRentalHistoryView(LoginRequiredMixin, ListView):
    model = Rental # Rental.objects.all()
    template_name = 'rentals/detail.html'

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Rental.objects.filter(Q(book__isbn=book_id) | Q(book__id=book_id))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs.get('book_id')
        obj = Book.objects.filter(Q(isbn=book_id) | Q(id=book_id)).first()
        #obj = get_object_or_404(Book, Q(isbn=book_id) | Q(id=book_id))
        context['object'] = obj
        #context['book_id'] = book_id
        return context

    # def get_queryset(self):
    #     book_id = self.kwargs.get('book_id')
    #     return Rental.objects.filter(Q(book__isbn=book_id) | Q(book__id=book_id))
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     qs = self.get_queryset()
    #     obj = None
    #     if qs.exists():
    #         obj = qs.first()
    #     context['object'] = obj
    #     return context    

class UpdateRentalStatusView(LoginRequiredMixin, UpdateView):
    model = Rental
    template_name = 'rentals/update.html'
    fields = ("status",)

    def get_success_url(self):
        book_id = self.kwargs.get('book_id')
        return reverse('rentals:detail', kwargs={'book_id':book_id})
        