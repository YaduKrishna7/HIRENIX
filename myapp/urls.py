from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [


    # Authentication URLs
    path('signup/', views.candidate_signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    #home page for candidates
    path('candidate/home/', views.candidate_home, name='candidate_home'),

]