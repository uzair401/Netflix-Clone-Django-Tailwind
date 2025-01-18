from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def movies(request):
    return render (request, 'movies.html')

def tv_shows(request):
    return HttpResponse("TV Shows Page")

def wishlist(request):
    return HttpResponse("Wishlist Page")