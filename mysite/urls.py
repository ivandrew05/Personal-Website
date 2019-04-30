from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('parallel', views.parallel, name='parallel'),
    path('fanfiction', views.fanfiction, name='fanfiction'),
    path('contact', views.contact, name='contact'),
    path('carousel1', views.carousel1, name='carousel1'),
    path('video1', views.video1, name='video1'),
    path('video2', views.video2, name='video2'),
    path('video3', views.video3, name='video3'),
    path('video4', views.video4, name='video4'),
    path('video5', views.video5, name='video5'),
    path('video6', views.video6, name='video6'),
    path('video7', views.video7, name='video7'),
    path('album1', views.album1, name='album1'),
    path('album2', views.album2, name='album2'),
    path('album3', views.album3, name='album3'),
    path('album4', views.album4, name='album4'),
    path('album5', views.album5, name='album5'),
    path('album6', views.album6, name='album6'),
]
