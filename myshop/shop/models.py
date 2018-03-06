# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True)

    class Meta:
        ordering=('name')
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])

class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products')
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True)
    
