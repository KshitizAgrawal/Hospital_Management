from django.db import models


class login(models.Model):
    Username= models.CharField(max_length=30)
    Password = models.CharField(max_length=30)