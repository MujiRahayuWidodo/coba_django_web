from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
from .models import DiamondItem 

def home(request):
    items = DiamondItem.objects.all()
    return render(request, 'home.html', {'items':items})