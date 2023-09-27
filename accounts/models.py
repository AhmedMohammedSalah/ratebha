from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
# from django.contrib.auth.models import Permission


def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "users/%s/%s.%s" % (instance.username, instance.username, extension)
def image_upload2(instance, filename):
    image_name, extension = filename.split(".")
    return "services/%s/%s.%s" % (instance.user.username, instance.user.username, extension)


class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_service_provider = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    services = (
        ("Photographer", "Photographer"),
        ("Makup_artist", "Makup-artist"),
        ("Hall_owner", "Hall owner"),
        ("Hotel_owner", "Hotel owner"),
        ("Car_gallary_owner", "Car gallary owner"),
        ("Shop_owner", "Shop owner"),
        ("Sound_System", "Sound System"),)
    service = models.CharField(
        max_length=30, choices=services, null=True, blank=True)
    image =models.ImageField(upload_to=image_upload, null=True, blank=True )
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class Services(models.Model):
    service_image=models.ImageField( upload_to=image_upload2, null=True, blank=True)
    service_date=models.DateField( auto_now=True, auto_now_add=False)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

