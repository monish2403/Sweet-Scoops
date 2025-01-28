from django.db import models

class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class reviews(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.URLField()
    review = models.TextField()
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    
class products(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.URLField()
    quantity = models.IntegerField()
    stock_status = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return self.name