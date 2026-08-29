from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    phone = forms.CharField(max_length=20, label="Phone Contact")
    email = forms.EmailField(label="Email")
    subject = forms.CharField(max_length=150, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message")