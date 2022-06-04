from django.db import models
from uuid import uuid4


class User(models.Model):

    user_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=11, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.first_name} - {self.phone}'

    class Meta:
        managed = True
        db_table = 'users'
