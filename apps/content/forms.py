from __future__ import absolute_import

from django.forms import ModelForm

from .models import Contact

class ContactForm(ModelForm):
  class Meta:
    model = Contact
    exclude = ('insert_date',)