from django.contrib.auth import logout
from django.utils import timezone

from django.shortcuts import render, redirect
from .models import CustomUser, CustomItem


# Create your views here.
def home(request):
    return render(request, "home.html")


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


def signup(request):
    role_choices = CustomUser.ROLES
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
    context = {
        'role_choices': role_choices
    }
    return render(request, 'signup.html')


def add_item(request):
    item_choices = CustomItem.ITEMS
    condition_choices = CustomItem.CONDITION
    lab_choices = CustomItem.LAB

    if request.method == "POST":
        item_name = request.POST['item_name']
        serial_number = request.POST['serial_number']
        condition = request.POST['condition']
        lab = request.POST['lab']

        try:
            item = CustomItem.objects.get(serial_number=serial_number)
            error_message = "Item with the same serial number already exists"
            return render(request, 'additem.html', {'error_message': error_message, 'item_choices': item_choices,
                                                    'condition_choices': condition_choices, 'lab_choices': lab_choices})
        except CustomItem.DoesNotExist:
            item = CustomItem(item_name=item_name, serial_number=serial_number, condition=condition, lab=lab)
            item.save()
            return redirect('additem')

    context = {
        'item_choices': item_choices,
        'condition_choices': condition_choices,
        'lab_choices': lab_choices
    }

    return render(request, 'additem.html', context)


def borrow_item(request):
    pass


# delete user
def delete_user(request, user_id):
    # Retrieve the user by ID
    try:
        user = CustomUser.objects.get(pk=user_id)
        user.delete()
    except CustomUser.DoesNotExist:
        pass

    return redirect('administrator')


def delete_item(request, item_id):
    # retrieve item by id
    try:
        item = CustomItem.objects.get(pk=item_id)
        item.delete()
    except CustomItem.DoesNotExist:
        pass
    return redirect("allitems.html")


def records(request):
    items = CustomItem.objects.all()
    return render(request, 'records.html', {'items': items})


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


def request_item(request):
    return render(request, 'request.html')


def student(request):
    return render(request, "student.html")


def administrator(request):
    return render(request, 'admin.html')
