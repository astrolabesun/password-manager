from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Credentials(models.Model):
    # one user can store 0 or more creds
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.URLField()
    # credentials can be either an email or username
    email_address = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    # is there a way to store this securely?
    # from my security course in uni, I know that I should hash and salt it
    # I just need to figure out how...
    password = models.CharField(max_length=100)
    expiry_date = models.DateTimeField(blank=True, null=True)