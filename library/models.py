from django.db import models

class ResourceType(models.TextChoices):
    DOCUMENT = 'document', 'Document(PDF, Word, PPT)'
    SLIDES = 'slides', 'Slides'
    VIDEO = 'video', 'Video(MP4)'
    AUDIO = 'audio', 'Audio(MP3,WAV)'
    IMAGE = 'image', 'Image(JPG,PNG)'

class  Resource(models.Model):
    """
    Resources includes Books, videos and audios,etc.
    """
    title = models.CharField(max_length=128,db_index=True)
    content_type = models.CharField(choices=ResourceType.choices)
    # reverse relationship of links 
    # reverse relationship of courses
    # reverse relationship of category
    url = models.URLField(unique=True,null=True,blank=True)
    file = models.FileField(upload_to="media/resources/",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ResourceCategory(models.Model):
    name = models.CharField(max_length=128)
    books = models.ManyToManyField(Resource, related_name='categories', blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Resource Categories' 

class Link(models.Model):
    url = models.URLField(unique=True)
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE,related_name='links')

    def __str__(self):
        return self.resource.title[:10] + self.url[:10]

class Course(models.Model):
    title = models.CharField(max_length=64)
    code = models.CharField(max_length=8)
    unit = models.CharField(max_length=2,null=True,blank=True)
    synopsis = models.TextField(null=True,blank=True)
    outline = models.TextField(null=True,blank=True)
    resource = models.ManyToManyField(Resource,related_name='courses',blank=True)

    def __str__(self):
        return self.code + self.title[:15]