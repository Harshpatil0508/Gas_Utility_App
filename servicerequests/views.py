from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import ServiceRequestForm
from .models import ServiceRequest

@login_required
def home(request):
    return render(request, 'servicerequests/home.html')

@login_required
def all_requests(request):
    all_requests = ServiceRequest.objects.all()
    return render(request, 'servicerequests/requests.html', {'all_requests': all_requests})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'servicerequests/request_submitted.html')
    else:
        form = ServiceRequestForm()
    return render(request, 'servicerequests/submit_request.html', {'form': form})

@login_required
def track_request(request, request_id):
    request_obj = ServiceRequest.objects.get(id=request_id)
    return render(request, 'servicerequests/track_request.html', {'request': request_obj})

@login_required
def track_request_by_id(request):
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        if request_id:
            return redirect('track_request', request_id=request_id)
    return render(request, 'servicerequests/home.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'servicerequests/login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'servicerequests/signup.html', {'form': form})
