from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Type(models.Model):
    type_ = models.CharField(max_length=50)

    def __str__(self):
        return self.type_
    

class Product(models.Model):
    name = models.CharField(max_length=50)

    # Upload Pic
    front_view = models.ImageField(upload_to="image/")
    back_view = models.ImageField(upload_to="image/")
    right_view = models.ImageField(upload_to="image/")
    left_view = models.ImageField(upload_to="image/")

    # Category and Type of product
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type_ = models.ForeignKey(Type, on_delete=models.CASCADE)
    

    # integer Fields
    ## logistic
    score = models.IntegerField()
    net_price = models.IntegerField()

    ## Supplier
    cost = models.IntegerField()
    cost_per_unit = models.IntegerField()
    discount = models.IntegerField()
    comp_offer = models.IntegerField()
    service_tax = models.IntegerField()
    vat = models.IntegerField()

    score = models.IntegerField()
    score = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.name
    
    