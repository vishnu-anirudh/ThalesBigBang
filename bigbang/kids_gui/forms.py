# make sure this is at the top if it isn't already
from django import forms

# our new form
class ContactForm(forms.Form):
    #contact_name = forms.CharField(required=True)
    your_name = forms.CharField(label='Your name', max_length=100, required=True)
    ##content = forms.CharField(
    #    required=True,
    #    widget=forms.Textarea
    #)

