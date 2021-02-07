from django.db import models

# Create your models here.
class Dish(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField(upload_to ='media/', blank=True)
    Price = models.IntegerField(default=0)

    def __str__(self):
        return self.Name