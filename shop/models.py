from django.db import models
from users.models import User


class Shop(models.Model):
    """ 
    Модель магазин
    """
    name = models.CharField(max_length=50, verbose_name='Название')
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    user = models.OneToOneField(User, verbose_name='Пользователь', related_name='shop_to_user',
                                blank=True, null=True,
                                on_delete=models.CASCADE)
    state = models.BooleanField(
        verbose_name='статус получения заказов', default=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.name
