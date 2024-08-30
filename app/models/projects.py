from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)  # Name of the project
    description = models.TextField()  # Detailed description of the project
    start_date = models.DateField()  # Start date of the project
    end_date = models.DateField(blank=True, null=True)  # End date (optional, in case the project is ongoing)
    url = models.URLField(max_length=200, blank=True, null=True)  # Link to the project or related site
    client = models.CharField(max_length=200, blank=True, null=True)  # Name of the client (if applicable)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the project was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the project was last updated
    status = models.CharField(
            max_length=20,
            choices=[('Pending', 'Pending'), ('Completed', 'Completed')],
            default='Pending'
        )
    def __str__(self):
        return self.name
