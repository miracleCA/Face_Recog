from django import forms
from .models import *

class ResgistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'face_id',
            'firstname',
            'lastname',
            'email',
            'phone',
            'department',
            'occupation',
            'job',
            'bio',
            'image'

        ]