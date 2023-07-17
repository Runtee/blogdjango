from django.urls import path
from . import views

handler404 = views.custom_404_page
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
]