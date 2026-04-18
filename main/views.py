from django.shortcuts import render
from django.views import View
from main.drive_api import start_resource_indexing
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Index(View):
    def get(self,request):
        return render(request,'main/index.html')

@method_decorator([login_required,],name='dispatch')
class Sync(View):
    def get(self,request):
        start_resource_indexing()
        return JsonResponse(data={'msg':'ok'})
