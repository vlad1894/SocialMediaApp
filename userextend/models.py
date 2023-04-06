from django.db import models
from django.contrib.auth.models import User



class UserToken(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.TextField(max_length=400)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


# Create your models here.
