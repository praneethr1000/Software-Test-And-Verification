from django.http import HttpResponse
from django.shortcuts import render, redirect
from .area_filters import AreaFilter
from .employee_filters import EmployeeFilter
from .employee_model import Employee
from .login_form import LoginForm
from .models import Bugtracker
from .forms import BugReportForm
from .filters import BugFilter
from .employee_form import EmployeeForm
from .program_filters import ProgramFilter
from .program_form import ProgramForm
from .area_form import AreaForm
from .program_model import Program
from .area_model import Area
from django.core import serializers


def bug_report_list(request):
    bug_reports = Bugtracker.objects.all()
    myFilter = BugFilter(request.GET, queryset=bug_reports)
    bug_reports = myFilter.qs
    context = {
        'bug_reports': bug_reports,
        'myFilter': myFilter
    }
    return render(request, 'bugtracker/list.html', context)


def create_bug_report(request):
    form = BugReportForm()

    if request.method == 'POST':
        form = BugReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bugReport-list')

    context = {
        'form': form,
    }
    return render(request, 'bugtracker/create.html', context)


def edit_bug_report(request, pk):
    bugReport = Bugtracker.objects.get(id=pk)
    form = BugReportForm(instance=bugReport)

    if request.method == 'POST':
        form = BugReportForm(request.POST, request.FILES, instance=bugReport)
        if form.is_valid():
            form.save()
            return redirect('bugReport-list')

    context = {
        'bugReport': bugReport,
        'form': form,
    }
    return render(request, 'bugtracker/edit.html', context)


def delete_bug_report(request, pk):
    bugReport = Bugtracker.objects.get(id=pk)
    if request.method == 'POST':
        bugReport.delete()
        return redirect('bugReport-list')

    context = {
        'bugReport': bugReport,
    }
    return render(request, 'bugtracker/delete.html', context)


# def login(request):
#     return render(request, 'bugtracker/login.html')
def login(request):
    # name = request.POST.get('name', '')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            employee = Employee.objects.get(user=form.cleaned_data['name'])
            if employee.level == '1':
                return redirect('no_db_access')
            else:
                return redirect('start-page')
                # return redirect('bugReport-list')
            # print(employee.level)
            # print(form.cleaned_data['name'])
            # return redirect('bugReport-list')

    context = {
        'form': form,
    }

    return render(request, 'bugtracker/login.html', context)


def employee_list(request):
    employees = Employee.objects.all()
    myFilter = EmployeeFilter(request.GET, queryset=employees)
    employees = myFilter.qs
    context = {
        'employees': employees,
        'myFilter': myFilter
    }
    return render(request, 'bugtracker/employee_list.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-list')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'bugtracker/edit_employee.html', context)


def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee-list')

    context = {
        'program': employee,
    }
    return render(request, 'bugtracker/delete_employee.html', context)


def export_employee(request):
    data = Employee.objects.all()
    L = []
    for i in data:
        s = str(i.id) + ' ' + str(i.user) + ' ' + str(i.loginID) + ' ' + i.level + "\n"
        for character in s:
            L.append(str(ord(character)))
    response = HttpResponse(''.join(L), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="employees.txt"'
    # return render(request, 'bugtracker/export_employee.html')
    # return response
    # form = Employee.get_form()
    # data = serializers.serialize("txt", Employee.objects.all())
    # response = HttpResponse(data, content_type='text/txt')
    # response['Content-Disposition'] = 'attachment; filename="areas.txt"'
    return response


def add_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'bugtracker/add_employee.html', context)


def program_list(request):
    programs = Program.objects.all()
    myFilter = ProgramFilter(request.GET, queryset=programs)
    programs = myFilter.qs
    context = {
        'programs': programs,
        'myFilter': myFilter
    }
    return render(request, 'bugtracker/program_list.html', context)


def edit_program(request, pk):
    program = Program.objects.get(id=pk)
    form = ProgramForm(instance=program)

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program-list')

    context = {
        'program': program,
        'form': form,
    }
    return render(request, 'bugtracker/edit_program.html', context)


def delete_program(request, pk):
    program = Program.objects.get(id=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('program-list')

    context = {
        'program': program,
    }
    return render(request, 'bugtracker/delete_program.html', context)


def add_program(request):
    form = ProgramForm()

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('program-list')

    context = {
        'form': form,
    }

    return render(request, 'bugtracker/add_program.html', context)


def area_list(request):
    areas = Area.objects.all()
    myFilter = AreaFilter(request.GET, queryset=areas)
    areas = myFilter.qs
    context = {
        'areas': areas,
        'myFilter': myFilter
    }
    return render(request, 'bugtracker/area_list.html', context)


def edit_area(request, pk):
    area = Area.objects.get(id=pk)
    form = AreaForm(instance=area)

    if request.method == 'POST':
        form = AreaForm(request.POST, request.FILES, instance=area)
        if form.is_valid():
            form.save()
            return redirect('area-list')

    context = {
        'area': area,
        'form': form,
    }
    return render(request, 'bugtracker/edit_area.html', context)


def delete_area(request, pk):
    area = Area.objects.get(id=pk)
    if request.method == 'POST':
        area.delete()
        return redirect('area-list')

    context = {
        'area': area,
    }
    return render(request, 'bugtracker/delete_area.html', context)


def export_area(request):
    data = serializers.serialize("xml", Area.objects.all())
    response = HttpResponse(data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename="areas.xml"'
    return response


def add_area(request):
    form = AreaForm()
    if request.method == 'POST':
        form = AreaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('area-list')

    context = {
        'form': form,
    }
    return render(request, 'bugtracker/add_area.html', context)


def home_page(request):
    return render(request, 'bugtracker/homepage.html')


def no_db_access_home_page(request):
    return render(request, 'bugtracker/no_db_access_home.html')


def start_page(request):
    return render(request, 'bugtracker/startpage.html')
