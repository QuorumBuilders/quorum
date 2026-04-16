from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'accounts'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('student/register/',views.RegisterView.as_view()),
    path('student/register/<str:freshman>/',views.RegisterView.as_view()),
        ]
router = DefaultRouter()
router.register(r'student/manage-profile',views.ManageStudentProfileViewset,basename='manage-profile')

urlpatterns += router.urls
