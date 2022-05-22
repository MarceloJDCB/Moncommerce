from django.urls import re_path
from django.urls import include
from rest_framework.routers import DefaultRouter
from userapp import views

app_name = "users"

router = DefaultRouter()

router.register(r'users', views.usersViewset)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    
]
