from django.db import models

class Entry (models.Model):

    user = models.CharField (max_length = 64)
    comment = models.CharField (max_length = 128)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__ (self):
        return self.user + ' : ' + self.comment
