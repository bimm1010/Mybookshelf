from django.db import models

# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    nametg = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    status = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to="static/", null=True, blank=True,default='default.jfif')
    
    

    def __str__(self):
        return self.name

    

