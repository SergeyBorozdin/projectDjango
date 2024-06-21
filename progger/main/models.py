from django.db import models


# Create your models here.
class Equipment(models.Model):
    title = models.CharField('Наименование', max_length=250)
    article = models.CharField('Артикул поставщика', max_length=250)
    lm_article = models.CharField('Артикул ЛМ', max_length=250)
    length = models.IntegerField('Длина')
    width = models.IntegerField('Ширина')
    depth = models.IntegerField('Высота')
    shop = models.CharField('Магазин', max_length=500)
    amount = models.IntegerField('Количество')
    address = models.CharField('Адрес хранения', max_length=250)
    image = models.ImageField(upload_to='image', blank=True, null=True)
    date = models.DateField('Дата')

    #    def __str__(self):
    #       return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись в реестр'
        verbose_name_plural = 'Реестр оборудования'
