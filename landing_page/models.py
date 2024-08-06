from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.


# class user (models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=15)
#     email = models.EmailField(max_length=254)
    

#     def __str__(self):
#         return f"{self.name} - phone_number: {self.phone_number} - email: {self.email}"


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    
class Book (models.Model):
    name =models.CharField(max_length=100,null=False,blank=False)
    email =models.EmailField(max_length=100,null=False,blank=False)
    phone =models.CharField(max_length=15,null=False,blank=False)
    date =models.CharField(max_length=20,null=False,blank=False)
    time =models.CharField(max_length=20,null=False,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
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