from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request,number):
    html = HttpResponse()
    html.write(f'hello world {number}')
    return html