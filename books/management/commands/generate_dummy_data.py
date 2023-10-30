from django.core.management.base import BaseCommand
from authors.models import Author
from publishers.models import Publisher
from books.models import BookTitle, Book
from customers.models import Customer
from django_countries.fields import Country
import random

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        # generating authors
        authors_list = ['John Smith', 'Adam Jones', 'Jane Johson', 'Megan Tyler']
        for name in authors_list:
            Author.objects.create(name=name)


        # generating publishers
        publishers_list = [
            {'name': 'X books', 'country': Country(code='us')},
            {'name': 'Bookz', 'country': Country(code='de')},
            {'name': 'Edu Mind', 'country': Country(code='gb')},
            {'name': 'Next', 'country': Country(code='pl')},
        ]
        for item in publishers_list:
            Publisher.objects.create(**item)


        # generating book title
        book_titles_list = ['Harry Zotter', 'Lorof the Wings', 'Django made easy', 'Switcher']
        publishers = [x.name for x in Publisher.objects.all()]
        items = zip(book_titles_list, publishers)

        for item in items:
            author = Author.objects.order_by('?')[0]
            publisher = Publisher.objects.get(name=item[1])
            BookTitle.objects.create(title=item[0], publisher=publisher, author=author)

        # generating books
        book_titles = BookTitle.objects.all()
        for title in book_titles:
            quantity = random.randint(1,5)
            for i in range(quantity):
                Book.objects.create(title=title)

        # generating customers
        customers_list = [ 
            {'first_name': 'John', 'last_name': 'Doe'},
            {'first_name': 'Adam', 'last_name': 'Harriz'},
            {'first_name': 'Lisa', 'last_name': 'Martinez'},
        ]

        for item in customers_list:
            Customer.objects.create(**item)