from django.urls import path
from .import views


urlpatterns = [
    path('my_app/', views.start_page, name='start_page'),
    path('work/', views.work, name='works'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),


]