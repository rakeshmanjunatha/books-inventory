# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Author,BookCategory,Books

# Register your models here.


admin.site.register(Author)
admin.site.register(Books)
admin.site.register(BookCategory)