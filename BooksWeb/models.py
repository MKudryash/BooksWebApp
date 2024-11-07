from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    yearPublish = models.IntegerField()
    image = models.ImageField(upload_to = 'media/')
    description = models.CharField(max_length=500)



class Feedback(models.Model):
    nameUser = models.CharField(max_length=50)    
    title = models.CharField(max_length=50)    
    email = models.EmailField(max_length=50)    
    feedback = models.CharField(max_length=500)    
    rating = models.IntegerField()
