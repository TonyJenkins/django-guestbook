from django import forms
from guestbookapp.models import Entry

class EntryForm (forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('user', 'comment', )