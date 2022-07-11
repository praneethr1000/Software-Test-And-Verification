from django.db import models

program_choices = (
    ('vscode', 'VS Code'),
    ('pycharm', 'Pycharm'),
    ('sublime', 'Sublime Text'),
    ('sqlserver', 'SQL Server'),
    ('notepad++', 'Notepad ++'),
    ('outlook', 'Outlook'),
)

report_type = (
    ('coding_error', 'Coding Error'),
    ('design_issue', 'Design Issue'),
    ('suggestion', 'Suggestion'),
    ('documentation', 'Documentation'),
    ('hardware', 'Hardware'),
    ('query', 'Query'),
)

severity = (
    ('mild', 'Mild'),
    ('medium', 'Medium'),
    ('infectious', 'Infectious'),
    ('minor', 'Minor'),
    ('serious', 'Serious'),
    ('fatal', 'Fatal'),
)

reported_by = (
    ('praneeth', 'Praneeth'),
    ('shruthi', 'Shruthi'),
)


# Create your models here.
class Bugtracker(models.Model):
    program = models.CharField(max_length=20, choices=program_choices, default='vscode')
    report_type = models.CharField(max_length=20, choices=report_type, default='coding_error')
    severity = models.CharField(max_length=20, choices=severity, default='mild')
    problem_summary = models.TextField()
    reported_by = models.CharField(max_length=20, choices=reported_by, default='praneeth')
    date = models.DateField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.program
