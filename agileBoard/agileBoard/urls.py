
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logIn',views.logIn),
    path('signUp',views.signUp),
    path('home',views.home),
    path('profile',views.profile)
]
