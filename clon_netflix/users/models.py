from django.db import models

# Create your models here.
class UserM(models.Model):
    """user model"""

    user = models.CharField(max_length=50, unique=True)

    title = models.TextField(max_length=60)
    picture = models.ImageField(upload_to='users/pictures')
    website = models.URLField(max_length=200)

    description = models.TextField(max_length=400, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=75)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    