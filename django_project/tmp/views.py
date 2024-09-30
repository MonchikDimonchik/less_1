from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Привет джанго.")


def catalog(request):
    return HttpResponse('Catalog')