from django.db import models

# Create your models here.
class Book (models.Model):
    b_name= models.CharField(max_length=30)
    pub_date=models.DateField("date_published")

class Shops (models.Model):
    cus_name= models.CharField(max_length=50)
    order= models.IntegerField()
    p_img = models.ImageField(upload_to='images/',blank=True)
    