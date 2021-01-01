from django.db import models

# Create your models here.
class User(models.Model):
    """user model"""

    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    country = models.CharField(max_length=50,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.username)
    