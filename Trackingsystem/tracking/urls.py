from django.urls import path,include
from tracking import views

urlpatterns = [
    


    path('',views.home, name="home"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('contactus/', views.contactUs, name="contactus"),
    path('track/', views.search, name="search"),
    path('form/', views.formtest, name="form"),
]
