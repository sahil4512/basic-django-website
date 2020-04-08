from django.db import models

# Create your models here.
class About(models.Model):
    vision = models.TextField()
    mission = models.TextField()
    image = models.ImageField(upload_to='about/%Y/%m/%d')
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)