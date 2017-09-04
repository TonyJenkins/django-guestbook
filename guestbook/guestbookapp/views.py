from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from guestbookapp.models import Entry
from guestbookapp.forms import EntryForm

def index (request):

    if request.method == 'POST':
        form = EntryForm (request.POST)

        if form.is_valid ():
            form.save (commit = True)
        else:
            print (form.errors ())

    context = {}

    entry_list = Entry.objects.all ()
    context ['entries'] = entry_list

    form = EntryForm ()
    context ['form'] = form

    response = render (request, 'guestbookapp/index.html', context)
    return response

def delete_entry (request, entry_id):

    Entry.objects.filter (id = entry_id).delete ()

    return redirect (reverse ('index'))