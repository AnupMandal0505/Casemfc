# your_app/models.py

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    founded_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    mission = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
