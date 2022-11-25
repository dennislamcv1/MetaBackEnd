from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Little Lemon !")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu for Little Lemon")

def book(request):
    return HttpResponse("Make a booking")
