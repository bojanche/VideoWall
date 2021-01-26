from django.db import models

# Create your models here.


class Asset(models.Model):
    name = models.CharField(max_length=256)
    path = models.CharField(max_length=512)
    created = models.DateTimeField(auto_now=True)
    creator = models.CharField(max_length=512)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
