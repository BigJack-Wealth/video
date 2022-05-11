import re
from unicodedata import name
from xml.dom.minidom import Document
from django.urls import path, include, re_path
from .import views



# app_name ="movie"

urlpatterns = [
    path('', views.home, name="home"),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('movielist/', views.movielist, name='movielist'),
    path('moviegrid/', views.moviegrid, name='moviegrid'),
    path('videod/', views.videod, name='videod'),
    path('about/', views.about, name='about'),
    
    #movies
    path('charted/', views.charted, name='charted'),
    path('bat/', views.bat, name='bat'),
    path('mat/', views.mat, name='mat'),
    path('mob/', views.mob, name='mob'),
    path('moon/', views.moon, name='moon'),
    path('tib/', views.tib, name='tib'),
    path('old/', views.oldguard, name='old'),
    path('dune/', views.dune, name='dune'),
    path('x/', views.x, name='x'),
    path('ecanto/', views.ecanto, name='ecanto'),
    path('cellar/', views.cellar, name='cellar'),
    path('river/', views.river, name='river'),
    path('yesday/', views.yesday, name='yesday'),
    path('stow/', views.stow, name='stow'),
    path('vivo/', views.vivo, name='vivo'),
    path('kot/', views.kot, name='kot'),
    path('turn', views.turn, name='turn'),
    path('blog/', views.blog, name='blog'),
    path('pnv', views.pnv, name='pnv'),
   
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    

]
