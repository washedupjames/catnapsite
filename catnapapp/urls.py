from django.urls import path
from . import views                                                                                                             

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('videos/', views.videos, name='videos'),
    path('gigs/', views.gigs, name='gigs'),
    path('login_user/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),



    path('video1/', views.video1, name='video1'),

]
