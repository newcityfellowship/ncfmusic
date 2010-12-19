from django.forms import ModelForm

from ncfmusic.apps.content.models import Contact

class ContactForm(ModelForm):
  class Meta:
    model = Contact
    exclude = ('insert_date',)