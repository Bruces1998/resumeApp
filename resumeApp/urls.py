from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'resumeApp'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('skill/', views.SkillCreate.as_view(),name='skill'),
    path('education/', views.EducationCreate.as_view(), name='education'),
    path('work_experience/',views.Work_ExperienceCreate.as_view(), name='work_experience'),
    path('profile/', views.ProfileCreate.as_view(), name='profile'),
    path('summary/', views.ProfileDetail.as_view(), name='summary'),
]
