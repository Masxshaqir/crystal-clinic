from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Book (models.Model):
    name =models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(max_length=100,null=False,blank=False)
    phone = models.CharField(max_length=15,null=False,blank=False)
    date =models.CharField(max_length=20,null=False,blank=False)
    time =models.CharField(max_length=20,null=False,blank=False)
    class Meta:
        unique_together = ('date', 'time')
    
    def __str__(self) -> str:
        return self.name + ' - ' + self.email 
    
    def clean(self):
        super().clean()
        if Book.objects.filter(date=self.date, time=self.time).exists():
            raise ValidationError(
                ('Booking already exists for the specified date and time: %(date)s at %(time)s'),
                params={'date': self.date, 'time': self.time},
            )
            
class Comment (models.Model):
    comment =models.CharField(max_length=300,null=False,blank=False)
    
    
    def __str__(self) -> str:
        return self.comment 