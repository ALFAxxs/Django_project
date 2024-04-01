from django import forms
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        if password:
            user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('type', 'A')
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(username, password, **extra_fields)


class Customer(AbstractUser):
    user_types = (
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('A', 'Admin'),
    )
    sex_choice = (('F', 'Female'), ('M', 'Male'))

    type = models.CharField(max_length=1, choices=user_types, default='A')
    gender = models.CharField(choices=sex_choice, max_length=1)
    #date_of_birth = models.DateField()
    #about_me = models.TextField('About me', blank=True)

class CourseTable(models.Model):
    Days = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('Free', 'Free')
    )
    # day_list = models.TextField('Days', choices=Days)
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=150, blank=False, null=False)
    Description = models.TextField()
    CoursePrice = models.DecimalField(max_digits=10, decimal_places=2)
    Instructor_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Course_Days = models.CharField(choices=Days, max_length=20)

class EnrollmentTable(models.Model):
    ID = models.AutoField(primary_key=True),
    course_id = models.ForeignKey(CourseTable, on_delete=models.CASCADE)
    User_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
class EnrollmentForm(forms.Form):
    course_id = forms.IntegerField(widget=forms.HiddenInput())