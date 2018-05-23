from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.


class Articles(models.Model):
    Title = models.CharField(max_length=50)
    Cover = models.ImageField(upload_to='image/%Y/%m/%d', default='photo.jpg')
    Content = UEditorField('write your content', height=100, width=500, default='test', imagePath="uploadimg/",
                            toolbars='mini', filePath='upload', blank=True)
    ResourceUrl=models.CharField(max_length=200, default='')
    ResourcePwd = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.Title
