# adminapp urls.py router file
from django.urls import path
from adminapp import views


# Template tagging
app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('videomgmt', views.video_mgmt, name='videomgmt'),
    path('testplayer', views.test_player, name='testplayer'),
]
