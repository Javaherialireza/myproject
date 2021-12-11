from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os
from django.core.exceptions import ValidationError

def validate_file_extention(value):
    ext = os.path.splitext(value.name)[1]
    vlid_extentions = [".jpg",'.png']
    if not ext.lower() in vlid_extentions:
        raise ValidationError("unsupprted file extension.")

# Create your models here.
class userprofile(modles.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to="files/user/avatar",null= True,blank=True, validators=[validate_file_extention])
    description = models.models.CharField( max_length=500,null=False,blank=False)

class article(models.Model):
    title =models.CharField(max_length=140,null=False, blank=False)
    cover = models.FileField(upload_to="files/article_cover/",null=False,blank=False , validators=[validate_file_extention])
    content = richtextfield()
    created_at = models.DateTimeField(default=datetime.now , blank=False)
    category = models.ForeignKey('category', on_delete = models.CASCADE)
    author = models.OneToOneField(userprofile, on_delete = models.CASCADE(collector, field, sub_objs, using))

class category(models.Model):
    title = models.CharField(max_length=128 , null=False , blank=False)
    cover = models.FileField(upload_to="files/category_cover" , null=False , blank= False, validators=[validate_file_extention])
