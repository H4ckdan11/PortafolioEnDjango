from django.shortcuts import render
from ..models import Portafolio

def home(request):
    portafolios = Portafolio.objects.all()
    return render(request, 'home.html', {'portafolios': portafolios})