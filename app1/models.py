from django.db import models
from django.utils import timezone

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255) 

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255) 

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255) 
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Filter_Price(models.Model):
    FILTER_PRICE= (
        ('100 TO 200','100 TO 200'), 
        ('200 TO 600','200 TO 600'),
        ('600 TO 900','600 TO 900'),
        ('900 TO 2000','900 TO 2000'),



    ) 
    price=models.CharField(choices=FILTER_PRICE,max_length=60)

    def __str__(self):
        return self.price


class  Product(models.Model):

    CONDITION=(('New','New'),('Old','Old'))
    STOCK=(('IN STOCK','IN STOCK'),('OUT  OF STOCK',' OUT OF STOCK'))
    STATUS=(('Publish','Publish'),('Draft','Draft'))

    unique_id=models.CharField(unique=True,max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='Product_images/img')
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    condition=models.CharField(choices=CONDITION,max_length=100)
    information=models.TextField()
    description=models.TextField()
    stock=models.CharField(choices= STOCK,max_length=200)
    status=models.CharField(choices=STATUS,max_length=200)
    created_date=models.DateTimeField(default=timezone.now)

    categories=models.ForeignKey(Categories,on_delete=models.CASCADE) 
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE) 
    color=models.ForeignKey(Color,on_delete=models.CASCADE) 
    filter_price=models.ForeignKey(Filter_Price,on_delete=models.CASCADE)



def save(self,*args,**kwargs):
    if self.unique_id is None and self.created_date and self.id:
        self.unique_id=self.created_date.strftime('75%Y%m%d23') + str(self.id)
    return super().save(*args,**kwargs )

def __str__(self):
        return self.image


class Images(models.Model):
    image=models.ImageField(upload_to='Product_images/img')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

class Tag(models.Model):
    name=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

