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

functional_area = (
    ('database', 'Database'),
    ('network', 'Network'),
    ('application', 'Application'),
    ('front_end', 'Front End'),
    ('deployment', 'Deployment'),
    ('fatal', 'Fatal'),
)

assigned_to = (
    ('group', 'Group'),
    ('manager', 'Manager'),
)

status = (
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('resolved', 'Resolved'),
)

priority = (
    ('Fix immediately', 'Immediately - 1'),
    ('Fix as soon as possible', 'ASAP - 2'),
    ('Fix before next milestone', 'Before Next Milestone - 3'),
    ('Fix before release', 'Before Release - 4'),
    ('Fix if possible', 'If Possible - 5'),
    ('Optional', 'Optional - 6'),
)

resolution = (
    ('pending', 'Pending'),
    ('fixed', 'Fixed'),
    ('irreproducible', 'Irreproducible'),
    ('deferred', 'Deferred'),
    ('as designed', 'As Designed'),
    ('cannot be fixed', 'Cannot be fixed'),
    ('withdrawn by reported', 'Withdrawn by Reporter'),
    ('need more info', 'Need More Info'),
    ('disagree with suggestion', 'Disagree with Suggestion'),
)

resolution_version = (
    ('Fix immediately', 'Immediately'),
    ('Fix as soon as possible', 'ASAP'),
    ('Fix before next milestone', 'Before Next Milestone'),
    ('Fix before release', 'Before Release'),
    ('Fix if possible', 'If Possible'),
    ('Optional', 'Optional'),
)

resolved_by = (
    ('Fix immediately', 'Immediately'),
    ('Fix as soon as possible', 'ASAP'),
    ('Fix before next milestone', 'Before Next Milestone'),
    ('Fix before release', 'Before Release'),
    ('Fix if possible', 'If Possible'),
    ('Optional', 'Optional'),
)

tested_by = (
    ('Fix immediately', 'Immediately'),
    ('Fix as soon as possible', 'ASAP'),
    ('Fix before next milestone', 'Before Next Milestone'),
    ('Fix before release', 'Before Release'),
    ('Fix if possible', 'If Possible'),
    ('Optional', 'Optional'),
)


# Create your models here.
class Bugtracker(models.Model):
    program = models.CharField(max_length=20, choices=program_choices, default='vscode')
    report_type = models.CharField(max_length=20, choices=report_type, default='coding_error')
    severity = models.CharField(max_length=20, choices=severity, default='mild')
    problem_summary = models.TextField(default='summary')
    # TODO: 1. Update the new field here
    problem = models.TextField(default='problem')
    suggested_fix = models.TextField(default='code')
    reproducible = models.TextField(default='NO')
    functional_area = models.CharField(max_length=20, choices=functional_area, default='database')
    assigned_to = models.CharField(max_length=20, choices=assigned_to, default='default')
    comments = models.TextField(default='comment')
    status = models.CharField(max_length=20, choices=status, default='open')
    priority = models.CharField(max_length=100, choices=priority, default='optional')
    resolution = models.CharField(max_length=100, choices=resolution, default='pending')
    resolution_version = models.CharField(max_length=100, choices=resolution_version, default='1.0')
    resolved_by = models.CharField(max_length=100, choices=resolved_by, default='abc@bughound.com')
    resolved_date = models.DateField(default='2022-07-15')
    tested_by = models.CharField(max_length=100, choices=tested_by, default='abc@bughound.com')
    tested_date = models.DateField(default='2022-07-15')
    treated_as_deferred = models.TextField(default='NO')

    reported_by = models.CharField(max_length=20, choices=reported_by, default='praneeth')
    date = models.DateField(default='2022-07-15')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.program
