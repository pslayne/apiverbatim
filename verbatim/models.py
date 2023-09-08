from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Texts(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='owner_user'
    )
    text = models.TextField()


