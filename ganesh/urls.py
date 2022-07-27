
from django.contrib import admin
from django.urls import path
from .views import helloworld,function,function1,live,cultural,donation,list1,poojaevents,index,video_feed,list2,livecam_feed

urlpatterns = [
    path('home/', helloworld,name='home'),
    path('donation/', donation,name='donate'),
    path('pooja/',list2,name='pooj'),
    path('live/',live,name='live'),
    path('cultural/',cultural,name='cul'),
    path('gotramlist/', list1,name='list'),
    path('bookpooja/',poojaevents,name='pooja'),
    path('', index, name='index'),
    path('video_feed', video_feed, name='video_feed'),
    path('livecam_feed', livecam_feed, name='livecam_feed'),

]

