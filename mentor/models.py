from django.db import models
from django.contrib.auth.hashers import make_password


class Mentor(models.Model):
    full_name = models.CharField(max_length=100)
    bio=models.TextField()
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    image=models.ImageField(upload_to="mentor_images")
    isStudent=models.BooleanField()
    experience=models.IntegerField()
    skills=models.TextField()
    

    def __str__(self):
        return self.full_name

class Course(models.Model):
    name=models.CharField(max_length=100)
    isFree=models.BooleanField()
    description=models.TextField()
    mentor=models.ForeignKey(Mentor, on_delete=models.CASCADE)
     #on_delete=models.CASCADE will delete the course if the mentor is deleted
    price=models.DecimalField(max_digits=6, decimal_places=2,)


   
    
    def __str__(self):
        return self.name
    
class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def _str_(self):
        return self.email


