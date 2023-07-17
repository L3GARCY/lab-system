from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('student/', views.student, name="student"),
    path('technician/', views.technician, name='technician'),
    path('administrator/', views.administrator, name="administrator"),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('logout/', views.logout_view, name='logout'),
    path("additem/",views.add_item,name="additem"),
    path("records/",views.records,name="records"),
    path("request_item/",views.request_item,name="request_item"),
]
