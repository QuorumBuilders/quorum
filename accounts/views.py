from rest_framework import generics
from rest_framework.permissions import AllowAny
from accounts.serializers import RegisterSerializer, FreshmanRegisterSerializer
from accounts.models import CustomUser as User

class RegisterView(generics.CreateAPIView):
    """
    POST:
    fields: username, matric_no, password
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Anyone can sign up
    
    def get_serializer_class(self):
        
        if self.kwargs.get('freshman') == 'freshman':
            return FreshmanRegisterSerializer
        else:
            return RegisterSerializer