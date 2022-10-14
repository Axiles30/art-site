from django.contrib.auth.views import LoginView
from django.urls import path
from .import views
from .views import ProfilePage, RegisterView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    path(r'^accounts/register/$', RegisterView.as_view(), name="register"),
    path('my_app/', views.start_page, name='start_page'),
    path('work/', views.work, name='works'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),


]