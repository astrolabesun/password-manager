from django_cryptography.fields import encrypt
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Credentials(models.Model):
    # one user can store 0 or more creds
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100)
    website = encrypt(models.URLField())
    # credentials can be either an email or username
    email_address = encrypt(models.EmailField(blank=True, null=True))
    username = encrypt(models.CharField(max_length=100, blank=True, null=True))
    # password field will store the encrypted password
    password = encrypt(models.CharField(max_length=100))
    expiry_date = encrypt(models.DateTimeField(blank=True, null=True))
