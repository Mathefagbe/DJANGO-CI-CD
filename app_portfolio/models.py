from django.db import models
from .constant import SPECIAL_CHARS_REGEX
import re

class Skills(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    icon=models.FileField(null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Projects(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/project/{filename}".format(filename=filename),
        )
        return url
    image_url=models.ImageField(upload_to=upload_to,null=True)
    tags=models.ManyToManyField(Skills)
    title=models.CharField(max_length=200,null=False,blank=False)
    body=models.TextField(null=False,blank=False)
    slug=models.SlugField(max_length=200,null=False,blank=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeFieldE(auto_now_add=True)


class ProjectKeyFeature(models.Model):
    project=models.ForeignKey(Projects,on_delete=models.CASCADE,null=True,related_name="key_features")
    title=models.CharField(max_length=200,null=False,blank=False)

class AboutMe(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/aboutMe/{filename}".format(filename=filename),
        )
        return url
    image_url=models.ImageField(upload_to=upload_to,null=True)
    body=models.TextField(null=False,blank=False)

class WorkExperience(models.Model):
    company=models.CharField(max_length=500,null=False,blank=False)
    title=models.CharField(max_length=500,null=False,blank=False)
    project=models.OneToOneField(Projects,on_delete=models.CASCADE,null=True,related_name="experience")
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    
class Experience(models.Model):
    title=models.CharField(max_length=500,null=False,blank=False)
    experience=models.ForeignKey(WorkExperience,on_delete=models.CASCADE,null=False,related_name="experiences")


# class Service(models.Model):
#     title=models.CharField(max_length=500,null=False,blank=False)
#     body=models.TextField(null=False)