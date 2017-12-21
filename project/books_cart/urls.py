from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view()),
    url(r'^add-books/', views.SubmitBookDetails.as_view(), name='add_books'),
    url(r'^add-category/', views.SubmitCategory.as_view(), name='add_category'),
    url(r'^add-author/', views.SubmitAuthorDetails.as_view(), name='add_author'),
]