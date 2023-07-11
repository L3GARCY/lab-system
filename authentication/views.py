from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser,CustomItem
from django.utils import timezone

from django.contrib.auth import authenticate, login, logout
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, "home.html")


from django.shortcuts import render, redirect
from .models import CustomUser

from django.shortcuts import render, redirect
from .models import CustomUser


# sign in view
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = CustomUser.objects.get(username=username)
            if user.password == password:
                if user.role == 'student':
                    return render(request, 'student.html', {'username': user.username, 'role': user.role})
                elif user.role == 'technician':
                    return render(request, 'technician.html', {'username': user.username, 'role': user.role})
                elif user.role == 'admin':
                    users = CustomUser.objects.all()
                    return render(request, 'admin.html', {'users': users})
            else:
                error_message = 'Invalid username or password!'
                return render(request, 'signin.html', {'error_message': error_message})
        except CustomUser.DoesNotExist:
            error_message = 'Invalid username or password!'
            return render(request, 'signin.html', {'error_message': error_message})
    return render(request, 'signin.html')

    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        role = request.POST['role']

        if password != confirm_password:
            error_message = 'Passwords do not match!'
            return render(request, 'signup.html', {'error_message': error_message})

        try:
            user = CustomUser.objects.get(username=username)
            error_message = 'Username already exists!'
            return render(request, 'signup.html', {'error_message': error_message})
        except CustomUser.DoesNotExist:
            user = CustomUser(username=username, password=password, role=role)
            user.save()
            return redirect('signin')

    return render(request, 'signup.html')


# delete user
def delete_user(request, user_id):
    # Retrieve the user by ID
    try:
        user = CustomUser.objects.get(pk=user_id)
        user.delete()
    except CustomUser.DoesNotExist:
        pass

    return redirect('admin')


def logout_view(request):
    # Store the logout time
    if request.user.is_authenticated:
        user = request.user
        user.last_logout = timezone.now()
        user.save()

    # Perform logout
    logout(request)

    return redirect('signin')

def technician(request):
    # Retrieve the choices for the dropdown fields from the CustomItem model

    return render(request, 'technician.html')

def student(request):
    return render(request, "student.html")
def admin(request):
    return render(request, 'admin.html')
