from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>I am here to fuck</h1>")
