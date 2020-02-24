from django.db import models


# Create your models here.
from website import settings


class BaseModel(models.Model):
    update_at = models.DateField(auto_now=True)
    create_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Profile(BaseModel):
    image = models.ImageField(upload_to=settings.IMAGES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class BaseInformationModel(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=True, null=True)


class Documents(BaseInformationModel):
    departmental = models.SmallIntegerField(blank=True, null=True)


class Practices(BaseInformationModel):
    pass


class Project(BaseInformationModel):
    pass


class Images(BaseModel):
    image = models.ImageField(upload_to=settings.IMAGES)
    name = models.CharField(max_length=100)
