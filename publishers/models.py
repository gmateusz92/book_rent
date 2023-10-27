from django.db import models
import uuid
from django_countries.fields import CountryField

# pipi install django-countries
# Create your models here.
class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #django sam nadaje id wiec po chuj to
    name = models.CharField(max_length=200)
    country = CountryField(blank_label= '(select country)')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} from {self.country}"