# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from djmoney.models.fields import MoneyField
from PIL import Image
# Create your models here.


class Author(models.Model):
	"""docstring for Author"""
	name = models.CharField(max_length=100,null=True)
	email = models.EmailField(max_length=50,null=True,blank=True)
	address = models.TextField(max_length=255,null=True,blank=True)
	def __str__(self):
		return self.name
		
class BookCategory(models.Model):
	"""docstring for BookCategory"""
	name = models.CharField(max_length=255,null=True)
	description = models.TextField(max_length=500,null=True,blank=True)

	def __str__(self):
		return self.name

		

class Books(models.Model):
	"""docstring for Books"""
	name = models.CharField(max_length=255,null=True)
	title = models.CharField(max_length=255,null=True,blank=True)
	category = models.ForeignKey(BookCategory,related_name="category",null=True,blank=True)
	author = models.ForeignKey(Author,related_name="author",null=True,blank=True)
	price = MoneyField(max_digits=10, decimal_places=2)
	publish_date = models.DateTimeField(null=True,blank=True)
	book_front_image=models.ImageField(upload_to='book_image/')
	book_path = models.FileField(upload_to='book_path/') 
	is_most_popular= models.BooleanField(default=False)

	def __str__(self):
		return self.name	

		