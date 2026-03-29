from django.contrib import admin
from .models import Resource,ResourceCategory,Link,Course

admin.site.register(Resource)
admin.site.register(ResourceCategory)
admin.site.register(Link)
admin.site.register(Course)
