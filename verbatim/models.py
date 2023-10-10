from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    username = models.CharField(null=True)
    email = models.CharField(max_length=100, unique=True)
    roles = models.CharField(max_length=255, null=False, default='Client')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Texts(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='owner_user'
    )
    text = models.TextField()


