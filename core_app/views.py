from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello, World!")

def movies(request):
    return HttpResponse("Movies Page")

def tv_shows(request):
    return HttpResponse("TV Shows Page")

def wishlist(request):
    return HttpResponse("Wishlist Page")