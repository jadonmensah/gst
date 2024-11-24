"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import re_path
from . import views

urlpatterns = [
    re_path("api/login", views.login),
    re_path("api/signup", views.signup),
    re_path("api/test-token", views.test_token),
    re_path("api/group/submit-time", views.submit_study_time),
    re_path("api/group/join", views.join_group),
    re_path("api/group/leave", views.leave_group),
    re_path("api/group/leaderboard", views.get_leaderboard),
    re_path("api/group/get-info", views.get_group_info),
    re_path("api/group/set-info", views.set_group_info),
    re_path("api/group/create", views.create_group),
]
