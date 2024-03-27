from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Accounts.models import Customer, CourseTable

def way(request):
    return render(request, 'signUp.html')

def home_page(request):
    return render(request, 'Home.html')

def student_profile(request, pk):
    user = get_object_or_404(Customer, id=pk)
    return render(request, 'student_profile.html', context={'student': user})

def teacher_profile(request, pk):
    user = get_object_or_404(Customer, id=pk)
    return render(request, 'teacher_profile.html', context={'user': user})

def Coursesview(request):
    courses = CourseTable.objects.all()
    return render(request, 'Courses.html', {'courses': courses})


def AddNewCourse(request):
    if request.method == 'POST':

        CourseTable.objects.create(
            Title=request.POST.get('Title'),
            Description=request.POST.get('Description'),
            CoursePrice=request.POST.get('CoursePrice'),
            Course_Days=request.POST.get('Course_Days'),
            Instructor_ID=instructor  # Set the instructor for the course
        )

        return redirect(f'/teacherprofile/{instructor.pk}')
    return render(request, 'AddNewCourse.html')


def login_post(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user:
            print('User is authenticated')
            if user.type == 'S':
                return redirect(f'/studentprofile/{user.pk}/')
            elif user.type == 'T':
                return redirect(f'/teacherprofile/{user.pk}/')
    return render(request, 'login.html')
def registration(request):
    if request.method == 'POST':
        password = request.POST.get('Password')
        user = Customer.objects.create(
            username=request.POST.get('Username'),
            first_name=request.POST.get('FirstName'),
            last_name=request.POST.get('LastName'),
            email=request.POST.get('Email'),
            type=request.POST.get('type'),  # Changed from 'Role' to 'type'
            gender=request.POST.get('Gender'),
            date_of_birth=request.POST.get('DateBirth')
        )
        if password:
            user.set_password(password)  # Hash the password
            user.save()
            return redirect('/login')
    return render(request, 'registration.html')
