# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.views import View
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from forms import AddBooksForm, AddCategoryForm, AddAuthorDetailsForm
from . import models

# Create your views here.
class Index(View):
	"""docstring for index"""
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		books_object=models.Books.objects.all()
		books_category=models.BookCategory.objects.all()
		return render(request, self.template_name,locals())

@method_decorator(login_required, name='dispatch')
class SubmitBookDetails(FormView):
	"""docstring for SubmitBookDetails"""
	form_class=AddBooksForm
	template_name='add_books.html'

	def form_valid(self, form):
		# a = form.save(commit=False)
		form.save()
		messages.success(self.request, 'Book added succesfsully.')
		return HttpResponseRedirect(self.get_success_url())
		
	def get_success_url(self):
		return reverse('add_books')

@method_decorator(login_required, name='dispatch')
class SubmitCategory(FormView):
	"""docstring for SubmitCategory"""
	form_class=AddCategoryForm
	template_name='add_category.html'
	def form_valid(self,form):
		form.save()
		messages.success(self.request, 'Category added successfully.')
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('add_category')

@method_decorator(login_required, name='dispatch')
class SubmitAuthorDetails(FormView):
	"""docstring for SubmitAuthorDetails"""
	form_class=AddAuthorDetailsForm
	template_name='add_author.html'

	def form_valid(self,form):
		form.save()
		messages.success(self.request,'Author details added successfully.')
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('add_author')
		