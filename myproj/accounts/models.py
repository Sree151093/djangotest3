from django.db import models
# Create your models here.

class PersonalDetails(models.Model):
    Name = models.CharField('Full Name',max_length=50,default='Junk')
    Age = models.IntegerField('What is your Age ?',default=0)

    
    def is_qualified(self):
        if self.Age > 21 :
            return f'Congrats {self.Name}, you are admitted to the University !'
        else:
            return f'Sorry {self.Name}, you are too young to join our University!'

    



class AcademicDetails(models.Model):
    UGperc = models.IntegerField(default=0)
    def __str__(self):
        return f'UG % is {self.UGperc}'
