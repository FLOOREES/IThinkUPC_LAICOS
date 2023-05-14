from django.urls import path
from . import views

app_name = "members"
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("questions/", views.questions_request, name= "questions"),
    path("generate/", views.generate_request, name= "generate"),
    path("clear/", views.clear_request, name= "clear"),
    path('myscript/', views.myscript, name='myscript'),
    path('register_study_slot/', views.register_study_slot, name='register_study_slot'),
]