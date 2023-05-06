from django.db import models


class Kab(models.Model):
    num = models.CharField(max_length=10, unique=True, verbose_name="номер")


    def __str__(self):
        return self.num
    
    class Meta:
        verbose_name = "Кабинет"

        verbose_name_plural = "Кабинеты"
    
        
class Inventar(models.Model):
    name = models.CharField(max_length=40, verbose_name="Наименование")
    num = models.CharField(max_length=40,  unique=True, verbose_name="Номер")
    num_kab = models.ForeignKey(Kab, on_delete=models.DO_NOTHING, verbose_name="Номер кабинета")
    response = models.CharField(max_length=40, verbose_name="Ответственный")
    count = models.CharField(max_length=5, verbose_name="Количество")

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Инвентарь"

        verbose_name_plural = "Инвентарь"
    


# Create your models here.
