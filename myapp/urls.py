from django.urls import path, include
from django.contrib import admin
from .import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [


    # Authentication URLs
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),
    path('signup/', views.candidate_signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    #home page for candidates
    path('candidate/home/', views.candidate_home, name='candidate_home'),

]