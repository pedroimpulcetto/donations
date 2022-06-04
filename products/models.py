from django.db import models
from uuid import uuid4

from users.models import User


def image_name(instance, filename):
    return '/'.join(['images', str(instance.title)+str(instance.product_id), filename])


class Product(models.Model):

    product_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255, blank=False, null=False,)
    description = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=image_name, blank=True, null=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products', blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'products'
