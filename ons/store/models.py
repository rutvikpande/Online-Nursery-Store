from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category', blank=True)

    #to set correct plural for the model changing the name in the db 
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    #to create human readable formatting
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='product', blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    #to set correct plural for the model changing the name in the db 
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    #to create human readable formatting

    #to dispaly product name
    def __str__(self):
        return self.name
