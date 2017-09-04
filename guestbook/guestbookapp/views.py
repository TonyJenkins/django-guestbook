from django.shortcuts import render

from guestbookapp.models import Entry

def index (request):

    context = {}

    entry_list = Entry.objects.all ()
    context ['entries'] = entry_list

    response = render (request, 'guestbookapp/index.html', context)
    return response