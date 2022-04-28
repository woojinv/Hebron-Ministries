from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import EventForm
import uuid
import boto3
from .models import Ministry, Member, Event, Photo

# "constant" variables
S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'hebronministries'


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
    members_not_in_ministry = Member.objects.exclude(id__in = ministry.members.all().values_list('id'))
    # instantiate EventForm to be rendered in the template
    event_form = EventForm()
    return render(request, 'ministries/detail.html', { 
        'ministry': ministry,
        'event_form': event_form,
        'members': members_not_in_ministry
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


class EventCreate(CreateView):
    model = Event
    fields = '__all__'
    success_url = '/events/'

class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(DeleteView):
    model = Event
    success_url = '/events/'



class MinistryCreate(CreateView):
    model = Ministry
    fields = ['name', 'lead', 'description', 'number_of_members', 'members']

    # this inherited method is called when a 
    # valid ministry form is being submitted
    def form_valid(self, form):
        # assign the logged in user (self.request.user)
        form.instance.user = self.request.user # form.instance is the ministry
        # let the CreateView do it's job as usual
        return super().form_valid(form)





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

def assoc_member(request, ministry_id, member_id):
    Ministry.objects.get(id=ministry_id).members.add(member_id)
    return redirect('detail', ministry_id=ministry_id)


def add_photo(request, ministry_id):
    # photo_file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try: 
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to ministry_id or ministry  (if you have a ministry object)
            Photo.objects.create(url=url, ministry_id=ministry_id)
        except: 
            print('An error occurred uploading file to S3')
    return redirect('detail', ministry_id=ministry_id)

