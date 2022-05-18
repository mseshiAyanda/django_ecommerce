from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.store, name="store"),
    path('checkout/', views.store, name="store"),
]
    

