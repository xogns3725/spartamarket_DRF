from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='./products/')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title
