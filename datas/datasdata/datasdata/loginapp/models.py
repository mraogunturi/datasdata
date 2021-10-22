from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class SignupForm(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    username = models.CharField(max_length=150, null=True)
    password = models.CharField(max_length=150, null=True)
    confirmpassword = models.CharField(max_length=150, null=True)
    # signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.username
