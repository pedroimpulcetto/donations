from django.db import models
from uuid import uuid4

from users.models import User
from .status import Status


def image_name(instance, filename):
    return f"{instance.product_id}-{filename}"


class Product(models.Model):

    product_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=image_name, blank=True, null=True)
    user_id_donor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products', blank=False, null=False)
    user_id_recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=255, choices=Status.choices(), blank=False, null=False, default=Status.OPEN)

    class Meta:
        managed = True
        db_table = 'products'
