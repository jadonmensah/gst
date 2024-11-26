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
from django.urls import path, include
from .views import (CreateUserView, ManageUserView, LoginView, 
CreateGroupView, GetGroupInfoView, SetGroupInfoView, JoinGroupView, 
LeaveGroupView)

from knox import views as knox_views

urlpatterns = [
    path('api/auth/create/', CreateUserView.as_view(), name="create_user"),
    path('api/auth/profile/', ManageUserView.as_view(), name='user_profile'),
    path('api/auth/login/', LoginView.as_view(), name='knox_login'),
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path("api/group/create/", CreateGroupView.as_view(), name="create_group"),
    path("api/group/get-info", GetGroupInfoView.as_view(), name="get_group_info"),
    path("api/group/set-info", SetGroupInfoView.as_view(), name="set_group_info"),
    path("api/group/join", JoinGroupView.as_view(), name="join_group"),
    path("api/group/leave", LeaveGroupView.as_view, name="leave_group")
]
