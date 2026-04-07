from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name',]
        

