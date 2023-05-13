from django.shortcuts import render

# TODO: Move to templates, duh
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")
