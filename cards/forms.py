from django import forms
from .models import Profile,Subjects,cards
from django.contrib.auth.models import User


class CardForm(forms.ModelForm):
    class Meta:
        model = cards
        exclude = ['update_date', 'pub_date', 'user' ]
class SubjectForm(forms.Form):
   Subject=forms.CharField(label='Subject',max_length=20)


class Profileform(forms.ModelForm):
    class Meta:
        model= Profile
        exclude =['user']