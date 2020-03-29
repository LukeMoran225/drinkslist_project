from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'drinkslist/index.html')


def about(request):
    return HttpResponse("Drinks list about page.")


def contactus(request):
    return HttpResponse("Drinks list contact us page")

