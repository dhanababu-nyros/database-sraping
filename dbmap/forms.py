#!/usr/bin/env python
from django import forms
from django.forms import ModelForm
from dbmap.models import Databases, DB_TYPE


class DatabaseForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    type = forms.CharField(max_length=2, widget=forms.Select(choices=DB_TYPE), required=False)
    user = forms.CharField(max_length=100, required=False)
    passwd = forms.CharField(max_length=100, widget=forms.PasswordInput(), required=False)
    host = forms.CharField(max_length=40)
    path = forms.FileField(required=False)

