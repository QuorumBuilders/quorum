from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.serializers import RegisterSerializer, ManageProfileSerializer
from accounts.models import CustomUser as User

class RegisterView(generics.CreateAPIView):
    """
    POST:
    fields: username, matric_no, password
    endpoint: api/v0/accounts/student/register/

    GET: Method not allowed
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,) # Anyone can sign up


class ManageStudentProfileViewset(ModelViewSet):

    queryset = User.objects.only('username','email','first_name','last_name','phone')
    serializer_class = ManageProfileSerializer
    http_method_names = ['get','put','patch','head','options']
    #permission_classes = (IsAuthenticated)