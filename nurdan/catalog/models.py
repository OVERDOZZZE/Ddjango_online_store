from django.db import models

# Create your models here.


class Catalog(models.Model):
    title = models.CharField('Name', max_length=50)
    description = models.TextField('description')
    price = models.IntegerField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f'/catalog{self.id}'

from django.db import models

