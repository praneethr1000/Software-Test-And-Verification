from django.shortcuts import render, redirect
from .models import Bugtracker
from .forms import BugReportForm
from .filters import BugFilter


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
        form = BugReportForm(request.POST)
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
        form = BugReportForm(request.POST, instance=bugReport)
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
