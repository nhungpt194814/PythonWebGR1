from django.db import models
from django.conf import settings
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    full_name = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    address = models.TextField()
    image = models.ImageField(null=True)

    def _str_(self):
        return self.username
