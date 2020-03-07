from django import forms
from .models import fortest

class testform(forms.ModelForm):

    class Meta:
        model = fortest
        fields = ('testlogin', 'testpassword')