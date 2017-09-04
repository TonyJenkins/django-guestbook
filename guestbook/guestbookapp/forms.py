from django import forms
from guestbookapp.models import Entry

class EntryForm (forms.ModelForm):

    # def __init__ (self, *args, **kwargs):
    #     print ('#################', kwargs)
    #     self.user = kwargs.pop ('user')
    #     self.comment = kwargs.pop ('comment')
    #     super (EntryForm, self).__init__ (*args, **kwargs)

    class Meta:
        model = Entry
        fields = ('user', 'comment', )