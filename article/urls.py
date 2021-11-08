from django.contrib import admin
from django.urls import path

app_name = "article"


from .views import *
urlpatterns = [
    path('add_article/',add_article,name = "add_article"),
    path('detail/<int:id>/',detail,name="detail"),
    path('update/<int:id>/',update_article,name="update_article"),
    path('delete/<int:id>/',delete_article,name="delete_article"),
    path('add_comment/<int:id>/',add_comment,name="add_comment"),

]

