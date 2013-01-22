from django.forms import ModelForm

from ncfmusic.apps.content.models import Contact, ConferenceRegistration

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('insert_date',)

class ConferenceRegistrationForm(ModelForm):
    class Meta:
        model = ConferenceRegistration
        exclude = ('insert_date', 'has_paid', 'cost', 'pp_token', 'payer_id',)