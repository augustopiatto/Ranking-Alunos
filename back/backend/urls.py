"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.contrib import admin
from django.urls import path
from backend.views import student_view
from backend.views import grade_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', student_view.students),
    path('api/top-three-students/', student_view.get_top_three_students),
    path('api/top-ten-students/', student_view.get_top_ten_students),
    path('api/grades/', grade_view.post_student_grade),
]
