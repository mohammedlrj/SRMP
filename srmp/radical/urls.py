from django.urls import path
from . import views
# from .views import specialites

urlpatterns = [
    path("", views.home,name="home" ),
    path("inner/", views.innerpage),
    path("service/", views.service,name="services"),
    path("about/", views.propos,name="propos"),
    path("contact/", views.contact,name="contact"),
    path('recommend/',views.recommend_doctors, name='recommend_doctors'),
    path("produit/", views.produit,name="produit"),
    path('spécialités/', views.doctor_specialties, name='specialites'),

]
