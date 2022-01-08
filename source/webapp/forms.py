from django import forms

from webapp.models import Guest


class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = ['name', 'email', 'text']
        error_messages = {
            'name': {'required': 'Name is required to create a new guest'},
            'email': {'required': 'Email is required to create a new guest'},
            'text': {'required': 'Please write your review'}
        }


class FindForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name']

