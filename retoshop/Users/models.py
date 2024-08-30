from django.db import models

class UserDetails(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.CharField(max_length=60)
    Password = models.CharField(max_length=50)

