from django.forms import ModelForm
from .models import Credentials

class CredentialsForm(ModelForm):
    class Meta:
        model = Credentials
        fields = ['site_name', 'website', 'email_address', 'username', 'password', 'expiry_date']
