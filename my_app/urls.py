from django.urls import path
from .import views


urlpatterns = [
    path('my_app/', views.start_page, name='start_page'),

]