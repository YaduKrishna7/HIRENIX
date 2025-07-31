from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # if you're using a custom logout view
    path('signup/', views.choose_signup, name='choose_signup'),
    path('signup/employee/', views.employee_signup, name='employee_signup'),
    path('signup/company/', views.company_signup, name='company_signup'),

    # ✅ Add this:
    path('candidate/home/', views.candidate_home, name='candidate_home'),

    path('hr-dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('company-dashboard/', views.company_dashboard, name='company_dashboard'),

    # hr adding form
    path('add-hr/', views.add_hr_view, name='add_hr'),

]