from rest_framework.views import APIView
from main.drive_api import DriveService
from rest_framework.response import  Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from library.models import Resource, Course
from library.serializers import  (CourseSerializer, ResourceSerializer)

class CourseViewset(ReadOnlyModelViewSet):
    """
    get:
    Returns courses data.
    filters => level, unit.

    get(search):
    search by course title or course code
    filters => title, code

    authenticattion:
    - JWT required

    reponses:
    200: course data
    401: unauthorized
    400: bad request (e.g empty search query)
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = [IsAuthenticated,]
        
    @action(detail=False)
    def search(self,request):
        title = request.query_params.get('title') or ''
        code = request.query_params.get('code') or ''

        if title.strip() == '' and code.strip() == '':
            # returns 404 if query is empty
            return Response({'error':'Empty search query'},status=400)

        queryset = Course.objects.filter(title__icontains=title,code__icontains=code)
        serializer = CourseSerializer(queryset,many=True)
        return Response(serializer.data)
        

class ResourceViewset(ModelViewSet):
    """
    get:
    Returns resource data.
    filters => level, unit.

    get(search):
    Returns data from a search query
    filters => title, content_type

    authenticattion:
    - JWT required

    reponses:
    200: resource data
    401: unauthorized
    400: bad request (e.g empty search query)
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    #permission_classes = [IsAuthenticated,]

    @action(detail=False)
    def search(self,request):
        title = request.query_params.get('title') or '' 
        content_type = request.query_params.get('content_type') or ''

        if title.strip() == '' and content_type.strip() == '':
            # returns 404 if query is empty
            return Response({'error':'Empty search query'},status=400)

        queryset = Resource.objects.filter(title__icontains=title,content_type__icontains=content_type)
        serializer = ResourceSerializer(queryset,many=True)
        return Response(serializer.data)
    