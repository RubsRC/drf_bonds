from django.db import models

# Create your models here.


class Bond(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=9, decimal_places=4)
    total = models.IntegerField()

    def __str__(self):
        return self.name
