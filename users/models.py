from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username