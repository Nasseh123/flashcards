from django import forms
from .models import Profile,Subjects,cards
from django.contrib.auth.models import User

# class SubjectForm(forms.ModelForm):
#     class Meta:
#         model=Subjects
#         exclude=['']