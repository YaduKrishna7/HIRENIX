from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout , authenticate
from .forms import CustomLoginForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  

# Create your views here.



# authentication views

# views.py





def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)  # ✅ MUST pass request
        if form.is_valid():
            user = form.get_user()  # ✅ Correct way to get the user
            login(request, user)

            # ✅ Redirect based on role
            if user.is_employee:
                return redirect('candidate_home')
            elif user.is_hr:
                return redirect('hr_dashboard')
            elif user.is_company:
                return redirect('company_dashboard')
            elif user.is_superuser:
                return redirect('/admin/')
            else:
                messages.warning(request, "User role not defined.")
                return redirect('login')
        else:
            messages.error(request, "Invalid credentials.")
            print("Form errors:", form.errors)  # ✅ DEBUGGING
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


# =============================
# ✅ SIGNUP VIEWS
# =============================

def choose_signup(request):
    return render(request, 'choose_signup.html')


def employee_signup(request):
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_employee = True
            user.save()
            login(request, user)
            return redirect('login')  # ✅ Correct name here
    else:
        form = EmployeeSignUpForm()

    return render(request, 'registration/employee_signup.html', {'form': form})


def company_signup(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_company = True
            user.save()
            login(request, user)
            return redirect('company_dashboard')
    else:
        form = CompanySignUpForm()

    return render(request, 'registration/company_signup.html', {'form': form})


# =============================
# ✅ HOME / DASHBOARD VIEWS
# =============================

@login_required
def home_view(request):
    if hasattr(request.user, 'is_employee') and request.user.is_employee:
        return render(request, 'home.html', {'user': request.user})
    return HttpResponseForbidden("Access denied.")


@login_required
def hr_dashboard(request):
    if hasattr(request.user, 'is_hr') and request.user.is_hr:
        return render(request, 'hr_dashboard.html')
    return HttpResponseForbidden("Access denied.")


@login_required
def company_dashboard(request):
    if hasattr(request.user, 'is_company') and request.user.is_company:
        return render(request, 'company_dashboard.html')
    return HttpResponseForbidden("Access denied.")

@login_required
def candidate_home(request):
    return render(request, 'home.html')



#==============================
# ✅ HR ADDING VIEWS
#==============================
def add_hr_view(request):
    if request.method == 'POST':
        form = HRSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_dashboard')  # or a success page
    else:
        form = HRSignUpForm()
    return render(request, 'add_hr.html', {'form': form})