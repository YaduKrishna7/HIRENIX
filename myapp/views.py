from django.shortcuts import render, redirect
from .forms import CandidateSignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout , authenticate
from .forms import CustomLoginForm
from django.contrib import messages


# Create your views here.



# authentication views

def candidate_signup(request):
    if request.method == 'POST':
        form = CandidateSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # After registration
    else:
        form = CandidateSignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Redirect based on role
                if user.role == 'candidate':
                    return redirect('candidate_home')
                elif user.role == 'hr':
                    return redirect('hr_dashboard')  # You can add this view later
                elif user.role == 'company' or user.is_superuser:
                    return redirect('/admin/')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def candidate_home(request):
    if request.user.role != 'candidate':
        return HttpResponseForbidden("Access denied.")
    return render(request, 'candidate_home.html', {'user': request.user})


