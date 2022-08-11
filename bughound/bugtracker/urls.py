from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),

    path('home/', views.home_page, name='home'),
    path('login/', views.login, name='login'),
    path('no_db_access/', views.no_db_access_home_page, name='no_db_access'),

    path('startpage/', views.start_page, name='start-page'),

    path('bug/', views.bug_report_list, name='bugReport-list'),
    # path('', views.home_page, name='home'),
    path('create/', views.create_bug_report, name='create-bugReport'),
    path('edit/<int:pk>', views.edit_bug_report, name='edit-bugReport'),
    path('delete/<int:pk>', views.delete_bug_report, name='delete-bugReport'),

    path('employee/', views.employee_list, name='employee-list'),
    path('add/employee/', views.add_employee, name='add_employee'),
    path('edit/employee/<int:pk>', views.edit_employee, name='edit-employee'),
    path('delete/employee/<int:pk>', views.delete_employee, name='delete-employee'),
    path('export/employee/', views.export_employee, name='export-employee'),

    path('program/', views.program_list, name='program-list'),
    path('add/program/', views.add_program, name='add_program'),
    path('edit/program/<int:pk>', views.edit_program, name='edit-program'),
    path('delete/program/<int:pk>', views.delete_program, name='delete-program'),

    path('area/', views.area_list, name='area-list'),
    path('add/area/', views.add_area, name='add_area'),
    path('edit/area/<int:pk>', views.edit_area, name='edit-area'),
    path('delete/area/<int:pk>', views.delete_area, name='delete-area'),
    path('export/area/', views.export_area, name='export-area'),

]