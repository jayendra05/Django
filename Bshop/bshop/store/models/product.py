from django.db import models
from .category import Category

class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=500,default='',null=True,blank=True)
    image=models.ImageField(upload_to='products')

    # def __str__(self):
    #     return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Product.object.filter(category=category_id)
        else:
            return Product.get_all_products()



