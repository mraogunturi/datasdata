from django.db import models


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Developers(models.Model):
    developerName = models.TextField(blank=False)
    language = models.TextField(blank=True)
    company = models.TextField(blank=True)
    location = models.TextField(blank=True)

    def __str__(self):
        return self.developerName


class Apis(models.Model):
    carName = models.TextField(blank=False)
    model = models.TextField(blank=True)
    company = models.TextField(blank=True)
    country = models.TextField(blank=True)

    def __str__(self):
        return self.carName