from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from rest_framework import generics, authentication, permissions, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from knox.models import AuthToken

from .serializers import UserSerializer, AuthSerializer, GroupSerializer
from .models import Group

class CreateUserView(generics.CreateAPIView):
    """
    API view for user creation
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class LoginView(KnoxLoginView):
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    Manage authenticated user
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user


class CreateGroupView( generics.CreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
class GetGroupInfoView(generics.RetrieveAPIView):
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self):
        return get_object_or_404(Group, pk=self.request.GET.get("id", "-1"))
class SetGroupInfoView(generics.UpdateAPIView):
    # TODO implement api/group/set-info/
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, format=None):
        serializer = GroupSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        group_id = request.GET.get("id", "-1")
        group = get_object_or_404(Group, pk=group_id)
        # check if user a member of the group
        if request.user in group.members.all():
            # if so allow their request
            if "name" in serializer.validated_data.keys():
                group.name = serializer.validated_data["name"]
            
            if "description" in serializer.validated_data.keys():
                group.description = serializer.validated_data["description"]
            group.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class JoinGroupView(generics.UpdateAPIView):
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, format=None):
        group_id = request.GET.get("id", "-1")
        group = get_object_or_404(Group, pk=group_id)
        group.members.add(request.user)
        return Response(status=status.HTTP_202_ACCEPTED) 

class LeaveGroupView(generics.DestroyAPIView):
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, format=None):
        group_id = request.GET.get("id", "-1")
        group = get_object_or_404(Group, pk=group_id)
        group.members.remove(request.user)
        return Response(status=status.HTTP_202_ACCEPTED) 
