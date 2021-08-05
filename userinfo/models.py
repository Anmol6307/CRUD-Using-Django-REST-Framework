from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name