from django.db import models

# Create your models here.
class Vid_Url(models.Model):
    url = models.URLField(max_length=500)