from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'library'

router = DefaultRouter()
router.register(r'resources',views.ResourceViewset,basename='resources')
router.register(r'courses',views.CourseViewset,basename='courses')
urlpatterns = router.urls