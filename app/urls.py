from app import views

from django.urls import  path

urlpatterns = [
   path('',views.user_func,name='user')
]