from django.shortcuts import render
from .models import BookTitle
# Create your views here.
from django.views.generic import ListView, FormView
from .forms import BookTitleForm
from django.urls import reverse, reverse_lazy

class BookTitleListView(FormView, ListView):
    #model = BookTitle
    queryset = BookTitle.objects.all()
    template_name = 'books/main.html'
    context_object_name = 'qs'
    form_class = BookTitleForm
    #success_url = reverse_lazy('books:main')
    #ordering = ('created',)

    def get_success_url(self):
        return self.request.path #zwraca sciezke na ktorej obecnie znajduje sie uzytkownik

    def get_queryset(self):
        parameter = 's'
        return BookTitle.objects.filter(title__startswith=parameter)
    
    def form_valid(self, form):   
        form.save() 
        return super().form_valid(form)

        
# def book_title_list_view(request):
#     qs = BookTitle.objects.all()
#     context = {
#         'qs': qs
#     }
#     return render(request, 'books/main.html', context)




# from django.views.generic import ListView, FormView
# from .models import BookTitle
# from .forms import BookTitleForm
# from django.urls import reverse_lazy
# from django.contrib import messages

# class BookTitleListView(ListView, FormView):
#     model = BookTitle
#     template_name = 'books/main.html'
#     context_object_name = 'qs'
#     form_class = BookTitleForm
#     success_url = reverse_lazy('books:main')

#     def get_queryset(self):
#         parameter = self.kwargs.get('letter', 'a')
#         return BookTitle.objects.filter(title__startswith=parameter)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
#         context['letters'] = letters
#         context['selected_letter'] = self.kwargs.get('letter', 'a').upper()
#         return context



#     def form_invalid(self, form):
#         messages.error(self.request, "Form submission failed. Please correct the errors.")
#         return super().form_invalid(form)





    
    


