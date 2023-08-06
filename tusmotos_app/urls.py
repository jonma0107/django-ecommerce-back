from django.urls import path, include

from tusmotos_app import views

urlpatterns = [
  path('products-list/', views.ProductsList.as_view()),
]
