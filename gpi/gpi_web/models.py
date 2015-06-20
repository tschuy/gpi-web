import os

from django.db import models
from django.contrib.auth.models import User

from semantic_version.django_fields import VersionField

def version_file_name(instance, filename):
    filename = '/'.join(
        [instance.project.package_name,
        unicode(instance.version),
        '{}-{}.tar.gz'.format(
            instance.project.package_name,
            unicode(instance.version))])

    # remove file if it exists
    if os.path.exists(filename):
        os.remove(filename)
    return filename

class Release(models.Model):

    def __unicode__(self):
        return unicode(self.version)

    file = models.FileField(upload_to=version_file_name)
    version = VersionField()
    project = models.ForeignKey('Project')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Project(models.Model):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50)
    package_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User)
