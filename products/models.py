from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_image = models.FileField(upload_to="products/",blank=True,null=True)
    product_price = models.IntegerField()
    
    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ["id"]


