from django.urls import path, include
from django.contrib import admin
from aware.views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings







urlpatterns=[

    path('',views.layout),
    path('html',views.html),
    path('aware',views.aware),
    path('ques',views.ques),
    path('layout',views.layout),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),
    path('quiz/', views.quiz,name='quiz'),
]