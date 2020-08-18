from django.db import models
from datetime import *

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = " Network should be at least 3 characters"
        if 0 < len(postData['desc']) < 10:
            errors["desc"] = " Description should be at least 10 characters"
        
        year, month, day = postData['release_date'].split('-')
        if datetime(int(year), int(month), int(day)) > datetime.now():
            errors['release_date'] = "Release Date should be in the past"

        potentially_title = Show.objects.filter(title=postData['title'])
        if len(potentially_title) > 0:
            errors['title_exists'] = "Title should be unique"

        print(errors)
        return errors
    
    def update_validator(self, postData, show_id):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = " Network should be at least 3 characters"
        if 0 < len(postData['desc']) < 10:
            errors["desc"] = " Description should be at least 10 characters"
        
        year, month, day = postData['release_date'].split('-')
        if datetime(int(year), int(month), int(day)) > datetime.now():
            errors['release_date'] = "Release Date should be in the past"
        
        potentially_title = Show.objects.filter(title=postData['title']).exclude(id=show_id)
        if len(potentially_title) > 0:
            errors['title_exists'] = "Title should be unique"

        print(errors)
        return errors




class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()