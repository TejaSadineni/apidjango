from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    published_date = models.DateField()
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/')
    created_date = models.DateTimeField(auto_now_add=True)
