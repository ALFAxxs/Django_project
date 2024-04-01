from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages

from Accounts.models import Customer, CourseTable, EnrollmentTable, EnrollmentForm


def home_page(request):
    return render(request, 'Home.html')


# @login_required(login_url='/login')
def student_profile(request, pk):
    user = get_object_or_404(Customer, id=pk)
    enrolled_courses = EnrollmentTable.objects.filter(User_id=user)
    return render(request, 'student_profile.html', context={'student': user, 'enrolled_courses': enrolled_courses})
def teacher_profile(request, pk):
    profile = get_object_or_404(Customer, id=pk)
    user = request.user
    courses = CourseTable.objects.filter(Instructor_ID=profile)
    return render(request, 'teacher_profile.html', context={'profile': profile, 'user': user, 'courses': courses})


def Coursesview(request):
    courses = CourseTable.objects.all()
    return render(request, 'Courses.html', {'courses': courses})


def AddNewCourse(request, pk):
    if request.method == 'POST':
        instructor = Customer.objects.get(pk=pk)
        CourseTable.objects.create(
            Title=request.POST.get('Title'),
            Description=request.POST.get('Description'),
            CoursePrice=request.POST.get('CoursePrice'),
            Course_Days=request.POST.get('Course_Days'),
            Instructor_ID=instructor
        )
        return redirect('/Coursesview/')
    return render(request, 'AddNewCourse.html')

def CourseDescription(request, pk):
    try:
        course = CourseTable.objects.get(pk=pk)
        description = CourseTable.objects.get(pk=pk)
    except CourseTable.DoesNotExist():
        raise Http404
    #course = get_object_or_404(CourseTable, pk=pk)
    return render(request, 'CourseDescription.html', {'description': description, 'contact': course.Instructor_ID.email})

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
            gender=request.POST.get('Gender'),
            type=request.POST.get('type')
        )
        if password:
            user.set_password(password)  # Hash the password
            user.save()
            return redirect('/login')
    return render(request, 'registration.html')

def enroll_course(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            course_id = form.cleaned_data['course_id']
            user_id = request.user.id
            enrollment = EnrollmentTable(course_id_id=course_id, User_id_id=user_id)
            enrollment.save()
            return redirect('success')  # Redirect to success page
    else:
        form = EnrollmentForm()  # Initialize an empty form
    return render(request, 'membership.html', {'form': form})

