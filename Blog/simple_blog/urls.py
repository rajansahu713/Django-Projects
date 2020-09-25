from django.urls import path
from . import views

urlpatterns = [
    
    path('addblog/', views.createBlog, name ="create"),
    path('',views.index),


]