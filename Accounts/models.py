from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import render  # Add import statement for render


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
    date_of_birth = models.DateField()
    about_me = models.TextField('About me', blank=True)



"""Relationships:
User-Course Relationship:
Each course is associated with an instructor (User) who created it.
Each user (student or teacher) can be associated with multiple courses through the enrollment or instructor relationship """


class CourseTable(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=150, blank=False, null=False)
    Description = models.TextField()
    CoursePrice = models.DecimalField(max_digits=10, decimal_places=2)
    Instructor_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Course_Days = models.CharField(max_length=150)


"""Course-Assignment Relationship:
Each assignment belongs to a specific course.
Each course can have multiple assignments."""


class AssignmentTable(models.Model):
    ID = models.AutoField(primary_key=True)
    Course_id = models.ForeignKey(CourseTable, on_delete=models.CASCADE)
    Course_description = models.TextField()
    Title = models.CharField(max_length=150, blank=False)
    Deadline = models.DateField(blank=False, null=False)


"""Submission-Grade Relationship:
Each submission is graded and associated with a grade entry.
Each grade entry corresponds to a specific submission."""


class SubmissionTable(models.Model):
    ID = models.AutoField(primary_key=True)
    Assignment_ID = models.ForeignKey(AssignmentTable, on_delete=models.CASCADE)
    Student_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    text_submission = models.TextField()
    score = models.FloatField()
    feedback = models.TextField()


"""User-Submission Relationship:
Each submission is made by a specific user (student).
Each user can make multiple submissions."""


class GradeTable(models.Model):
    submission_id = models.ForeignKey(SubmissionTable, on_delete=models.CASCADE)
    grade = models.FloatField()
    comment = models.TextField()


"""User-Enrollment Relationship:
Each user (student) can enroll in multiple courses.
Each course can have multiple enrolled users."""


class EnrollmentTable(models.Model):
    ID = models.AutoField(primary_key=True),
    course_id = models.ForeignKey(CourseTable, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
