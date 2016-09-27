from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()


class ContactUsForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
