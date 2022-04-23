from django.db import models
from django.urls import reverse

# Create your models here.
class Ministry(models.Model):
    name = models.CharField(max_length=100)
    lead = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    number_of_members = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'ministry_id': self.id})
