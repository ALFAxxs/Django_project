from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path

from Accounts.views import login_post, registration, home_page , student_profile , teacher_profile, way, AddNewCourse, Coursesview

urlpatterns = [
    path('login/', login_post),
    path('registration/', registration),
    path('home/', home_page),
    path('teacherprofile/<int:pk>/', teacher_profile),
    path('studentprofile/<int:pk>/', student_profile),
    path('way/', way),
    path('AddNewCourse/', AddNewCourse),
    path('Coursesview/', Coursesview)
]