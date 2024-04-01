from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path

from Accounts.views import login_post, registration, home_page, student_profile, teacher_profile, \
    AddNewCourse, Coursesview, CourseDescription, enroll_course

urlpatterns = [
    path('login/', login_post),
    path('registration/', registration),
    path('home/', home_page),
    path('teacherprofile/<int:pk>/', teacher_profile),
    path('studentprofile/<int:pk>/', student_profile),
    path('AddNewCourse/<int:pk>/', AddNewCourse),
    path('Coursesview/', Coursesview),
    path('CourseDescription/<int:pk>/', CourseDescription),
    path('enroll/', enroll_course, name='enroll_course')
]