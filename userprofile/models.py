from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofie', on_delete=models.CASCADE)
