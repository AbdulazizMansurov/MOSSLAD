from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Mahsulot kategoriyasi', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriya'

    def get_4_products(self):
        return self.category.all()[:4]

class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name='Mahsulot nomi')
    price = models.FloatField(verbose_name='Mahsulot narxi', default=0)
    information = models.CharField(max_length=250, verbose_name="Mahsulot haqida informatsiya")
    image = models.ImageField(verbose_name="Rasmi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Saytga qo'yilgan vaqti")
    is_published = models.BooleanField(verbose_name="Saytga chiqazish", default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya", related_name='category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ['-created_at']