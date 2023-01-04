# Generated by Django 4.0.5 on 2023-01-04 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', django_cryptography.fields.encrypt(models.URLField())),
                ('email_address', django_cryptography.fields.encrypt(models.EmailField(blank=True, max_length=254, null=True))),
                ('username', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True))),
                ('password', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('expiry_date', django_cryptography.fields.encrypt(models.DateTimeField(blank=True, null=True))),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
