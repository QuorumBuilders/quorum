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
        
    @action(detail=False,methods=['GET'])
    def search(self,request):
        title = request.query_params.get('title')
        code = request.query_params.get('code')
        level = request.query_params.get('level')
        query = {}
        if title:
            query['title__icontains'] = title
        if code:
            query['code__icontains'] = code
        if level:
            query['level__icontains'] = level

        if len(query) == 0:
            # returns 404 if query is empty
            return Response({'error':'Empty search query'},status=400)

        queryset = Course.objects.filter(**query)
        serializer = CourseSerializer(queryset,many=True)
        return Response(serializer.data)
        

class ResourceViewset(ReadOnlyModelViewSet):
    """
    get:
    Returns resource data.
    filters => level, unit.

    get(search):
    Returns data from a search query
    filters => title, mime_type

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
        name = request.query_params.get('name')
        mime_type = request.query_params.get('mime_type')

        query = {}
        if name:
            query['name__icontains'] = name
        if mime_type:
            query['mime_type__icontains'] = mime_type

        if len(query) == 0:
            # returns 404 if query is empty
            return Response({'error':'Empty search query'},status=400)

        queryset = Resource.objects.filter(**query)
        serializer = ResourceSerializer(queryset,many=True)
        return Response(serializer.data)
    