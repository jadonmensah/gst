from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

@api_view(["POST"])
def login(request):
    user = get_object_or_404(User, email=request.data["email"])
    if not user.check_password(request.data["password"]):
        # SECURITY: do not change response
        # this response should be identical to when get_object_or_404 fails
        return Response(
            {"detail": "No User matches the given query."},
            status = status.HTTP_404_NOT_FOUND
        ) 
    token, _created = Token.objects.get_or_create(user=user)
    
    serializer = UserSerializer(instance=user)
    
    # remove stuff we don't want the user to see
    user_scrubbed = serializer.data
    del user_scrubbed["password"]
    del user_scrubbed["id"]

    return Response(
            {
                "token": token.key,
                "user": user_scrubbed,
            })

@api_view(["POST"])
def signup(request):
    # Attempt to create user object based on request data
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        
        # write user to db
        serializer.save() 
        
        # retrieve user we just wrote
        user = User.objects.get(email=request.data["email"])
        user.set_password(request.data["password"])
        user.save()

        # create JWT token for user
        token = Token.objects.create(user=user)

        # remove stuff we don't want the user to see
        user_scrubbed = serializer.data
        del user_scrubbed["password"]
        del user_scrubbed["id"]

        return Response(
            {
                "token": token.key,
                "user": user_scrubbed,
            })

    # 400 Bad Request if signup could not be performed for whatever reason
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({"passed": True})

@api_view(["POST"])
def submit_study_time(request):
    return Response({})

@api_view(["POST"])
def join_group(request):
    return Response({})

@api_view(["POST"])
def leave_group(request):
    return Response({})

@api_view(["GET"])
def get_leaderboard(request):
    return Response({})

@api_view(["GET"])
def get_group_info(request):
    return Response({})

@api_view(["POST"])
def set_group_info(request):
    return Response({})

@api_view(["POST"])
def create_group(request):
    return Response({})
