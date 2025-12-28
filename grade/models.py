from django.db import models
from student.models import StudentModel
# Create your models here.
class Grade(models.Model):
    grade_name = models.CharField(max_length=255)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)