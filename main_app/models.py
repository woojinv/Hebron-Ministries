from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('members_detail', kwargs={'member_id': self.id})



class Ministry(models.Model):
    name = models.CharField(max_length=100)
    lead = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    number_of_members = models.IntegerField()

    members = models.ManyToManyField(Member)
    # foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'ministry_id': self.id})



class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=250)
    contact = models.CharField(max_length=100)

    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} on {self.date}"

    class Meta:
        ordering = ['date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for ministry_id: {self.ministry_id} @{self.url}"


    
    
