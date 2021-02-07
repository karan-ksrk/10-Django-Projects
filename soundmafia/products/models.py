from django.db import models

class Product(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length = 220)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title