from django.urls import path, include

from tusmotos_app import views

urlpatterns = [
  path('products-list/', views.ProductsList.as_view()),
  path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]
