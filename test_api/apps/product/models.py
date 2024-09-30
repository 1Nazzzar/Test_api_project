from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('Название',max_length=100)
    description = models.TextField('Описание')
    quantity = models.PositiveIntegerField('Количество', default = 0)
    is_active = models.BooleanField('Активен', default=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)