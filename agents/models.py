from django.db import models

# Create your models here.

class Agents(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='agents/%Y/%m/%d')
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Agent'
        verbose_name = 'Agent'