from django.forms import ModelForm
from .models import Credentials

class CredentialsForm(ModelForm):
    class Meta:
        model = Credentials
        exclude = ['user_id']
