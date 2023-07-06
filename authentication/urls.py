from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.home,name="home"),
    path('signup.html/',views.signup,name="signup"),
    path('signin.html/',views.signin,name="signin"),
    path('student/',views.student,name="student"),
    path('technician/', views.technician, name='technician'),
    path('admin/',views.admin,name="admin"),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('logout/', views.logout_view, name='logout'),
    
]
