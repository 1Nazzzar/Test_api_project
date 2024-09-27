from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('name', max_length=200),
    description = models.CharField('description',)
    quantity = models.PositiveIntegerField('amount', default=0)
    is_active = models.BooleanField('Active', default=True),
    price = models.DecimalField('price')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
