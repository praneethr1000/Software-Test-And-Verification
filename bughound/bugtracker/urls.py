from django.urls import path
from . import views


urlpatterns = [
    path('', views.bug_report_list, name='bugReport-list'),
    # path('', views.home_page, name='home'),
    path('create/', views.create_bug_report, name='create-bugReport'),
    path('edit/<int:pk>', views.edit_bug_report, name='edit-bugReport'),
    path('delete/<int:pk>', views.delete_bug_report, name='delete-bugReport'),
    path('add/employee/', views.add_employee, name='add_employee'),
    path('add/program/', views.add_program, name='add_program'),
    # path('add/area/<str:program>', views.add_area, name='add_area'),
    path('add/area/', views.add_area, name='add_area'),
    path('home/', views.home_page, name='home'),

]