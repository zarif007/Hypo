from django.urls import path
from .import views

urlpatterns=[
    path('',views.First,name="home"),
    path('downnotes/',views.downnotes, name='downnotes'),
    path('downnotes/download/',views.downloadingNotes,name="downn"),
    path('downnotes/goback/',views.Back2HP,name="b2h"),
    path('downnotes/download/goback/',views.Back2HP,name="b2h"),

    path('downaudio/',views.downaudio, name='downaudio'),
    path('downaudio/download/',views.downloadingaudio,name="downa"),
    path('downaudio/goback/',views.Back2HP,name="b2h"),
    path('downaudio/download/goback/',views.Back2HP,name="b2h"),

    path('downvideo/',views.downvideo, name='downvideo'),
    path('downvideo/download/',views.downloadingVideo,name="downv"),
    path('downvideo/goback/',views.Back2HP,name="b2h"),
    path('downvideo/download/goback/',views.Back2HP,name="b2h"),
    

]