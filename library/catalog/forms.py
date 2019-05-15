from django import forms

class ContactForm(forms.Form):
	first_name = forms.CharField(label='First name', max_length=64)
	last_name = forms.CharField(label='Last_name', max_length=64)
	email = forms.EmailField(label='Email', max_length=64)
	subject = forms.CharField(max_length=128)
	message = forms.CharField(widget=forms.Textarea)