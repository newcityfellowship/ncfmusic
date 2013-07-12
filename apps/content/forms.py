from django.forms import ModelForm, TextInput, Textarea

from ncfmusic.apps.content.models import Contact, ConferenceRegistration

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('insert_date',)

class ConferenceRegistrationForm(ModelForm):
    class Meta:
        model = ConferenceRegistration
        exclude = ('insert_date', 'has_paid', 'cost', 'pp_token', 'payer_id', 'housing',)
        widgets = {
            'how_serving': Textarea(attrs={'rows': 4}),
            'skills': Textarea(attrs={'rows': 4}),
            'wanting_to_learn': Textarea(attrs={'rows': 4}),
            'special_housing_needs': Textarea(attrs={'rows': 4}),
        }
