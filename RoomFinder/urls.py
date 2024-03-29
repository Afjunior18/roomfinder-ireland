"""RoomFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from room import views

from room import views as room_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('add_room/', room_views.add_room, name='add_room'),
    path('approve/<int:room_id>/', views.approve_room, name='approve_room'),
    path('contact/', room_views.contact, name='contact'),
    path('delete/<int:room_id>/', views.delete_room, name='delete_room'),
    path('edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('room_finder/', room_views.room_finder, name='room_finder'),
    path('summernote/', include('django_summernote.urls')),
    path('', room_views.index, name='index'),
]
