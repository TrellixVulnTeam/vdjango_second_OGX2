from django.urls import path, include
from django.urls.resolvers import URLPattern

from photos import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/',
         views.ProductDetail.as_view()),



]
