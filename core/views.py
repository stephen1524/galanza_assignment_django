from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def base(request):
    return render(request, 'base.html', {'title': 'Base'}) 

def home(request):
    return render(request, 'home.html', {'title': 'Home'})  

def about(request):
    return render(request, 'about.html', {'title': 'About'})  
    
    

  