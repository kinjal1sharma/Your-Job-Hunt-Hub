from django.urls import path
from datetime import datetime
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns =[
    path("", views.index,name="times_jobs-home"),
    path("about",views.about,name="times_jobs-about"),
    path("creators",views.creators,name="times_jobs-creators"),
    path("search",views.search,name="times_jobs-search"),
    path("timesjobs",views.timesjobs,name="times_jobs-timesjobs"),
    path("scrapedtimes",views.adder_page,name="adder_page"),
    path("indeed",views.indeed,name="times_jobs-indeed"),
    path("scrapedindeed", views.page_adder, name="page_adder"),
    

]