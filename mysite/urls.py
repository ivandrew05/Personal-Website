from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    path('carousel1', views.carousel1, name='carousel1'),
    path('carousel2', views.carousel2, name='carousel2'),
    path('video1', views.video1, name='video1'),
    path('video2', views.video2, name='video2'),
    path('video3', views.video3, name='video3'),
    path('video4', views.video4, name='video4'),
    path('video5', views.video5, name='video5'),
    path('video6', views.video6, name='video6'),
    path('album2', views.album2, name='album2'),
]
