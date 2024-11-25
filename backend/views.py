from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics, authentication, permissions
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
        return Group.objects.get(pk=self.request.GET.get("id", "-1"))

class SetGroupInfoView(generics.UpdateAPIView):
    # TODO implement api/group/set-info/
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, format=None):
        pass