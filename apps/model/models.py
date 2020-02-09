from django.db import models


# Create your models here.
from website import settings


class Documents(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    file = models.FileField(upload_to=settings.DOCUMENTS, null=False, blank=False)
    departmental = models.SmallIntegerField(blank=True, null=True)
    update_at = models.DateField(auto_now=True)
    create_at = models.DateField(auto_now=True)


class Practices(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    file = models.FileField(upload_to=settings.PRACTICES, null=False, blank=False)
    update_at = models.DateField(auto_now=True)
    create_at = models.DateField(auto_now=True)
