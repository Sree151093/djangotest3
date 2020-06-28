from django.db import models

# Create your models here.
class TravelData(models.Model):
    place = models.CharField(max_length=20,default='')
    overview = models.TextField(max_length=300,default='')
    details = models.TextField(default='')
    date = models.DateField(default='')
    rating= models.IntegerField(default=1)
    img = models.ImageField(default='',upload_to='travel')

    def __str__(self):
        return self.place