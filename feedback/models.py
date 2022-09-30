from django.db import models
from authentication.models import User



class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50, null=True)
    last_name=models.CharField(max_length=50, null=True)
    reg_No=models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    address = models.TextField()
    session_year = models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Department(models.Model):
    department_id=models.AutoField(primary_key=True)
    department_name=models.TextField()

    

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students, on_delete=models.CASCADE , null=True)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    department_id=models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    unit_name=models.CharField(max_length=20)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    

    

   

