from django.shortcuts import render
from django.http import HttpResponse


# Ministry Class
class Ministry:
    def __init__(self, name, lead, description, number_of_members):
        self.name = name
        self.lead = lead
        self.description = description
        self.number_of_members = number_of_members

ministries = [
    Ministry('Finance Team', 'Alex Kim', 'The Finance Team supports other ministries by providing accurate and timely financial information and administrative services.', 3),
    Ministry('Worship Team', 'Peter Pak', 'Focusing all worship towards God.', 6),
    Ministry('Team Ignite', 'Jon Choe', 'Members of Team Ignite extend the love of Christ to everyone who walks through the doors of Hebron.', 10)
]









# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def ministries_index(request):
    return render(request, 'ministries/index.html', { 'ministries': ministries })