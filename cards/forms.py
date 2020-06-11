from django import forms
from .models import Profile,Subjects,cards
from django.contrib.auth.models import User

class SubjectForm(forms.Form):
   Subject=forms.CharField(label='Subject',max_length=20)