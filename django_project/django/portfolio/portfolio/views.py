from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text = {
        'name':"Vikrant Nandan",
        'age':"35",
        'mobile':"1234567890",
        'friend_name': ['rina', 'tina', 'dina', 'pina', 'gina', 'hina']
    }
    return render(request, 'index.html', text)
    # dataHome = "Get data from DB: This is our Home Page"
    # return HttpResponse(dataHome)

def about(request):
    return render(request, 'about.html')
    # dataAbout = "Get data from DB: This is our About Page"
    # return HttpResponse(dataAbout)

def contact(request):
    return render(request, 'contact.html')
    # dataContact = "Get data from DB: This is our Contact Page."
    # return HttpResponse(dataContact)