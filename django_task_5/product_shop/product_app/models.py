from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()
    price=models.DecimalField(decimal_places=2,max_digits=8)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name