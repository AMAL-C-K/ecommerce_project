from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images', default=1)

    def __str__(self):
        return self.category_name

    def get_categories_url(self):
        return reverse('categories', args=[self.slug])


class Brands(models.Model):
    brand_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.brand_name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    base_price = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    trending = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    offer = models.BooleanField(default=False)
    tag = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_product_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

