from django.http import HttpResponse

def home(request):
    dataHome = "Get data from DB: This is our Home Page"
    return HttpResponse(dataHome)

def about(request):
    dataAbout = "Get data from DB: This is our About Page"
    return HttpResponse(dataAbout)

def contact(request):
    dataContact = "Get data from DB: This is our Contact Page."
    return HttpResponse(dataContact)