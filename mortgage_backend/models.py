from django.db import models

# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    state_abbr = models.CharField(max_length=10)
    median_home_value = models.IntegerField()
    def __str__(self):
        return self.name