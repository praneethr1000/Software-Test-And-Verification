from django.shortcuts import render, redirect
from .models import Bugtracker


def bug_report_list(request):
    bug_reports = Bugtracker.objects.all()
    context = {
        'bug_reports': bug_reports,
    }
    return render(request, 'bugtracker/list.html', context)


def create_bug_report(request):
    return render(request, 'bugtracker/create.html')


def edit_bug_report(request, pk):
    return render(request, 'bugtracker/edit.html')


def delete_bug_report(request, pk):
    return render(request, 'bugtracker/delete.html')
