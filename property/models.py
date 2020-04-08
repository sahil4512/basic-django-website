from django.db import models

# Create your models here.

# choices for type
property_type = (
        ('sale', "Sale"),
        ('rent', "Rent")
    )

# property class


class Property(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True)
    property_type = models.CharField(choices=property_type, max_length=10)
    price = models.PositiveIntegerField()
    property_category = models.ForeignKey(
        'Category', null=True, 
        on_delete=models.SET_NULL
        )
    area = models.DecimalField(decimal_places=2 , max_digits=8)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/%Y/%m/%d' , null=True)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Property'
        verbose_name = 'Propertie'


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/%Y/%m/%d' , null=True)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name = 'Categorie'
      

class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes = models.TextField()
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Reserve'
        verbose_name = 'Reservation'


