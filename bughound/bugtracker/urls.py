from django.urls import path
from . import views

urlpatterns = [
    path('', views.bug_report_list, name='bug-list'),
    path('create/', views.create_bug_report, name='create-bugReport'),
    path('edit/', views.edit_bug_report, name='edit-bugReport'),
    path('delete/', views.delete_bug_report, name='delete-bugReport'),
]