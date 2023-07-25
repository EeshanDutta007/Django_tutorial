from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    peoples = [
        {'name' : 'Eeshan Dutta', 'age': 21},
        {'name' : 'Shivam Singh', 'age': 22},
        {'name' : 'Aditya Singh', 'age': 23},
        {'name': 'Achu Paji', 'age': 15}
    ]
    return render(request, 'index.html', context={'page' : 'Home Page', 'peoples': peoples})

def contact(request):
    return render(request, 'contact.html',  context={'page' : 'Contact Page'})

def about(request):
    return render(request, 'about.html', context={'page' : 'About Page'})
def success(request):
    print('*' * 10)
    return HttpResponse("<h1>Hey, This is a Success Page</h1>")