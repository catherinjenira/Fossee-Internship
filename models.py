from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=120)
    uploaded_at = models.DateTimeField(auto_now=True)
    summary = models.JSONField()

    def __str__(self):
        return self.name
