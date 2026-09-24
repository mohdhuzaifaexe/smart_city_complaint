from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Complaint, Category

def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('dashboard')

    return render(request, 'register.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def user_logout(request):

    logout(request)

    return redirect('home')


def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard.html')



def submit_complaint(request):

    if not request.user.is_authenticated:
        return redirect('login')

    categories = Category.objects.all()

    if request.method == 'POST':

        title = request.POST.get('title')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        address = request.POST.get('address')
        image = request.FILES.get('image')

        category = Category.objects.get(id=category_id)

        Complaint.objects.create(
            user=request.user,
            category=category,
            title=title,
            description=description,
            address=address,
            image=image
        )

        messages.success(
            request,
            'Complaint submitted successfully!'
        )

        return redirect('dashboard')

    return render(
        request,
        'submit_complaint.html',
        {
            'categories': categories
        }
    )

def my_complaints(request):

    if not request.user.is_authenticated:
        return redirect('login')

    complaints = Complaint.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'my_complaints.html',
        {
            'complaints': complaints
        }
    )