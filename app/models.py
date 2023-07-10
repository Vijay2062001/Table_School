from django.db import models

# Create your models here.

class Collage(models.Model):
    collage_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.collage_name
   
class Student(models.Model):
    collage_name=models.ForeignKey(Collage,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=40)
    student_id=models.IntegerField()
    student_rol=models.IntegerField()
    student_address=models.CharField(max_length=100)
    def __str__(self):
        return self.student_name
   