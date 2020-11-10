from django.db import models
from datetime import date
class ShowManager(models.Manager):
    def basic_validator(self,postData):
        today = date.today()
        errors = {}
        for show in Show.objects.all():
            if postData['title']== show.title:
                errors["title"] = "Show title already exist !!!!"  
            else:
                if len(postData['title']) < 2:
                    errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['desc']) > 1:
            if len(postData['desc']) < 10:
                errors["desc"] = "Show description should be at least 10 characters"
            else:
                pass
        if postData['date'] >= str(today):
            errors['date'] = "Show release date should be in the past"
        return errors
    def update_validator(self,postData,id):
        today = date.today()
        errors = {}
        for show in Show.objects.all():
            if show.id == id:
                if postData['title']== show.title:
                    pass
            else:
                if postData['title']== show.title:
                    errors["title"] = "Show title already exist !!!!" 
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['desc']) > 1:
            if len(postData['desc']) < 10:
                errors["desc"] = "Show description should be at least 10 characters"
            else:
                pass
        if postData['date'] >= str(today):
            errors['date'] = "Show release date should be in the past"
        return errors
class Show(models.Model):
    title = models.CharField(max_length=45 , unique=True )
    network = models.TextField()
    release_date = models.DateTimeField()
    desc = models.TextField(default="no description provided")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()