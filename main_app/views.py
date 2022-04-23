from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ministry


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def ministries_index(request):
    ministries = Ministry.objects.all()
    return render(request, 'ministries/index.html', { 'ministries': ministries })

def ministries_detail(request, ministry_id):
    ministry = Ministry.objects.get(id=ministry_id)
    return render(request, 'ministries/detail.html', { 'ministry': ministry })

class MinistryCreate(CreateView):
    model = Ministry
    fields = '__all__'

class MinistryUpdate(UpdateView):
    model = Ministry
    fields = ['name', 'lead', 'description', 'number_of_members']

class MinistryDelete(DeleteView):
    model = Ministry
    success_url = '/ministries/'