from django.db import models

# Create your models here.

class ball(models.Model):
    idx = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    dealSum = models.IntegerField()
    type = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    sizeNum = models.FloatField()
    class Meta:
        verbose_name = '球类'
        verbose_name_plural = '球类'

    def __str__(self):
        return self.name
