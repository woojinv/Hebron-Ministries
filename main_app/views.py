from django.shortcuts import render
from django.http import HttpResponse


# Ministry Class
class Ministry:
    def __init__(self, name, description, number_of_members):
        self.name = name
        self.description = description
        self.number_of_members = number_of_members

ministries = [
    Ministry('Finance Team', 'The Finance Team supports other ministries by providing accurate and timely financial information and administrative services. We desire to be faithful stewards of the financial resources God has given to Hebron EM in order to bring change to our community inside and outside. The finance team leads and oversees income (offerings and other designated contributions), expenses (spending and reimbursements), and other general financial administration according to guidelines approved in the Annual Budget and the Standard Operating Procedure.', 3),
    Ministry('Worship Team', 'We desire to be a ministry that serves the Church in humility and love – focusing all worship towards God, leading in joyful declaration of His love and faithfulness through Jesus Christ, and extending His healing, edification, and transformation through the Holy Spirit.', 6),
    Ministry('Team Ignite', 'Members of Team Ignite extend the love of Christ to everyone who walks through the doors of Hebron by relentlessly embracing people. We strive to provide an atmosphere of welcoming and encouraging through our hospitality ministry as well.', 10)
]









# Create your views here.
def home(request):
    return HttpResponse("<h1>Home</h1>")

def about(request):
    return render(request, 'about.html')

def index_ministries(request):
    return render(request, 'ministries/index.html', { 'ministries': ministries })