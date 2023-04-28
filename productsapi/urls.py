from django.urls import path
from productsapi import views

urlpatterns = [
    path('brands/', views.BrandList.as_view()),
    path('brands/<int:id>/', views.BrandDetails.as_view()),
    path('products/', views.ProductsList.as_view()),
    path('products/<int:id>/',views.ProductsDetails.as_view()),
    path('cart/', views.Cart_details.as_view()),
    
    
]   
    
    
    
