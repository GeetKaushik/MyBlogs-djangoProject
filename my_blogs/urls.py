from django.contrib import admin
from django.urls import path
from my_blogs import views

urlpatterns = [
    path("", views.home, name='my_blogs'),
    path("about", views.about, name='my_blogs'),
    path("services", views.services, name='my_blogs'),
    path("contact", views.contact, name='my_blogs'),
    path("subscription", views.subcription, name='my_blogs'),
    path("blog", views.blog, name='my_blogs'),
    path("ck",views.ck, name='my_blogs'),
    path("allblogs", views.allBlogs, name='my_blogs'),
    path("blogDetails/<str:blog_id>/", views.blogDetails, name='blogDetails'),
    path("loginusr", views.loginusr, name="loginusr"),
    path("signupusr", views.signupusr, name="signupusr"),
    path("logoutusr", views.logoutusr, name="logoutusr"),
]
