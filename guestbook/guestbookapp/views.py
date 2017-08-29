from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index (request):

    context = {}

    response = render (request, 'guestbookapp/index.html', context)
    return response