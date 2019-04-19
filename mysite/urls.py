from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    path('carousel1', views.carousel1, name='carousel1'),
    path('carousel2', views.carousel2, name='carousel2'),
]
