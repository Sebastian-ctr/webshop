from django.shortcuts import render
from .models import Home, Flower, About, Success, Contact

# Create your views here.
def home(request):
    queryset = Home.objects.first()
    context = {
        'content':queryset,
        }
    return render(request, 'home.html', context)

def shop(request):
    queryset = Flower.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, 'shop.html', context)

def about(request):
    queryset = About.objects.first()
    context = {
        'about':queryset,
    }
    return render(request, 'about.html', context)

def success(request):
    queryset = Success.objects.all()
    context = {
        'success':queryset,
    }
    return render(request, 'success.html', context)

def contact(request):
    querystet = Contact.objects.first()
    context = {
        'contact': querystet,
    }
    return render(request, 'contact.html', context)