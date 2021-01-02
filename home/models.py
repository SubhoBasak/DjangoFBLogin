from django.db import models


class LoginDetails(models.Model):
    email = models.CharField(max_length=500, null=True)
    password = models.CharField(max_length=500, null=True)
