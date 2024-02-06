from django.db import models

class Mentor(models.Model):
    full_name = models.CharField(max_length=100)
    bio=models.TextField()
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    image=models.ImageField(upload_to="mentor_images")

    def __str__(self):
        return self.full_name

class Course(models.Model):
    name=models.CharField(max_length=100)
    isFree=models.BooleanField()
    description=models.TextField()
    mentor=models.ForeignKey(Mentor, on_delete=models.CASCADE)
    #on_delete=models.CASCADE will delete the course if the mentor is deleted
    
    def __str__(self):
        return self.name