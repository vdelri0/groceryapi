from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.float_field()
    purchased = models.BooleanField(default=False)
    purchased_at = models.datetime_field(auto_now_add=True)
    updated_at = models.datetime_field(auto_now=True)