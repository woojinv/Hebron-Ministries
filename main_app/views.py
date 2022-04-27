from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ministry, Member, Event
from .forms import EventForm


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
    # instantiate EventForm to be rendered in the template
    event_form = EventForm()
    return render(request, 'ministries/detail.html', { 
        'ministry': ministry,
        'event_form': event_form
    })

def add_event(request, ministry_id):
    # create a ModelForm instance using the data in request.Post
    form = EventForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the ministry_id assigned to it. 
        new_event = form.save(commit=False)
        new_event.ministry_id = ministry_id
        new_event.save()
    return redirect('detail', ministry_id=ministry_id)


def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', { 'events': events })



def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {
        'event': event 
    })



class MinistryCreate(CreateView):
    model = Ministry
    fields = '__all__'

class MinistryUpdate(UpdateView):
    model = Ministry
    fields = ['name', 'lead', 'description', 'number_of_members']

class MinistryDelete(DeleteView):
    model = Ministry
    success_url = '/ministries/'


def members_index(request):
    members = Member.objects.all()
    return render(request, 'members/index.html', { 'members': members })

def members_detail(request, member_id):
    member = Member.objects.get(id=member_id)
    return render(request, 'members/detail.html', { 'member': member })


class MemberCreate(CreateView):
    model = Member
    fields = '__all__'

class MemberUpdate(UpdateView):
    model = Member
    fields = '__all__'

class MemberDelete(DeleteView):
    model = Member
    success_url = '/members/'