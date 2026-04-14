from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from main.drive_api import download_file, DriveService
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
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = [IsAuthenticated,]
        
    @action(detail=False)
    def search(self,request):
        title = request.query_params.get('title') or ''
        code = request.query_params.get('code') or ''
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
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    #permission_classes = [IsAuthenticated,]

    @action(detail=False)
    def search(self,request):
        title = request.query_params.get('title') or ''
        content_type = request.query_params.get('content_type') or ''
        queryset = Resource.objects.filter(title__icontains=title,content_type__icontains=content_type)
        serializer = ResourceSerializer(queryset,many=True)
        return Response(serializer.data)
    

class StreamMaterialView(APIView):
    def get(self, request, file_id):
        # 1. Fetch metadata first (small request)
        metadata = DriveService.files().get(fileId=file_id).execute()
        filename = metadata.get('name', 'document.pdf')
        filesize = int(metadata.get('size', 0))


        # 3. Stream the response
        response = StreamingHttpResponse(
            download_file(file_id=file_id),
            content_type=metadata.get('mimeType', 'application/octet-stream')
        )
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        # Providing Content-Length helps the browser show a progress bar
        if filesize:
            response['Content-Length'] = filesize
            
        return response