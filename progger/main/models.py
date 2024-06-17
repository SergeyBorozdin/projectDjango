from django.db import models


# Create your models here.
class Equipment(models.Model):
    article = models.CharField('Артикул поставщика', max_length=25)
    lm_article = models.CharField('Артикул ЛМ', max_length=25)
    name = models.CharField('Наименование', max_length=250)
    length = models.IntegerField('Длина')
    width = models.IntegerField('Ширина')
    depth = models.IntegerField('Высота')
    shop = models.CharField('Магазин', max_length=50)
    amount = models.IntegerField('Количество')
    address = models.CharField('Адрес хранения', max_length=25)
    image = models.ImageField(upload_to='equipment_photos/', blank=True, null=True)
    date = models.DateField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись в реестр'
        verbose_name_plural = 'Реестр оборудования'


    @property
    def has_photo(self):
        return bool(self.photo and hasattr(self.photo, 'url'))
