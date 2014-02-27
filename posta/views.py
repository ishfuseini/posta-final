from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Posta <br> <a href='/posta/about'>About</a>")

def about(request):
    return HttpResponse("About Posta <br> <a href='/posta/'>Index</a>")
