from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

def validate_file_extention(value):
    ext = os.path.splitext(value.name)[1]
    vlid_extentions = [".jpg",'.png']
    if not ext.lower() in vlid_extentions:
        raise ValidationError("unsupprted file extension.")

# Create your models here.
class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to="files/user/avatar",null= True,blank=True, validators=[validate_file_extention])
    description = models.CharField( max_length=500,null=False,blank=False)
    
    def __str__(self):
        return self.user.username


class article(models.Model):
    title =models.CharField(max_length=140,null=False, blank=False)
    cover = models.FileField(upload_to="files/article_cover/",null=False,blank=False , validators=[validate_file_extention])
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now , blank=False)
    category = models.ForeignKey('category', on_delete = models.CASCADE)
    author = models.OneToOneField(userprofile, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class category(models.Model):
    title = models.CharField(max_length=128 , null=False , blank=False)
    cover = models.FileField(upload_to="files/category_cover" , null=False , blank= False, validators=[validate_file_extention])

    def __str__(self):
        return self.title
    
