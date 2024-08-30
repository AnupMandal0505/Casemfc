from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)  # Name of the service
    description = models.TextField()  # Detailed description of the service
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the service was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the service was last updated

    def __str__(self):
        return self.name
