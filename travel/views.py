from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"home.html")

def destination(request):
    return render(request,"destination.html")

def deals(request):
    return render(request,"deals.html")

def contact(request):
    return render(request,"contact.html")