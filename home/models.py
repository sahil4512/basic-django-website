from django.db import models

# Create your models here.
class Services(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name = 'Service'