from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Version(models.Model):
    file = models.FileField()
    number = models.CharField(max_length=50)
    project = models.ForeignKey('Project')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Project(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User)
