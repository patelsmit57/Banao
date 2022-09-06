from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class User(AbstractUser):
    type = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor')
    )
    picture = models.ImageField(upload_to='photos/%Y/%m/%d')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField(validators=[MinValueValidator(100000),MaxValueValidator(999999)], null=True)
    Types_of_Users = models.CharField(choices=type, max_length=10, default=False)

    def __str__(self):
        return self.username
