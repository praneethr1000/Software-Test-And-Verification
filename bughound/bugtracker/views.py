from django.shortcuts import render, redirect

from .models import Bugtracker
from .forms import BugReportForm
from .filters import BugFilter
from .employee_form import EmployeeForm
from .program_form import ProgramForm
from .area_form import AreaForm


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


def add_program(request):
    form = ProgramForm()

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'bugtracker/add_program.html', context)


def add_area(request):
    form = AreaForm()
    if request.method == 'POST':
        form = AreaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'bugtracker/add_area.html', context)


def home_page(request):
    return render(request, 'bugtracker/homepage.html')