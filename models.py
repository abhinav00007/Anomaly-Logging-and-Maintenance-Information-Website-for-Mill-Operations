# anomaly_app/models.py

from django.db import models

class Anomaly(models.Model):
    mill_type = models.CharField(max_length=20)
    mill_operation = models.CharField(max_length=100)
    anomaly_description = models.TextField()

    def __str__(self):
        return f"{self.mill_type} - {self.mill_operation}"
