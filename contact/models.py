from django.db import models

# Create your models here.
class ContactDetails(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)

    class Meta():
        verbose_name = 'Contact Detail'
        verbose_name = 'Contact Detail'