from django.db import models

program_choices = (
    ('VS Code', 'VS Code'),
    ('Pycharm', 'Pycharm'),
    ('Sublime Text', 'Sublime Text'),
    ('SQL Server', 'SQL Server'),
    ('Notepad ++', 'Notepad ++'),
    ('Outlook', 'Outlook'),
)

report_type = (
    ('Coding Error', 'Coding Error'),
    ('Design Issue', 'Design Issue'),
    ('Suggestion', 'Suggestion'),
    ('Documentation', 'Documentation'),
    ('Hardware', 'Hardware'),
    ('Query', 'Query'),
)

severity = (
    ('Mild', 'Mild'),
    ('Medium', 'Medium'),
    ('Infectious', 'Infectious'),
    ('Minor', 'Minor'),
    ('Serious', 'Serious'),
    ('Fatal', 'Fatal'),
)

reported_by = (
    ('Praneeth', 'Praneeth'),
    ('Shruthi', 'Shruthi'),
)

functional_area = (
    ('Database', 'Database'),
    ('Network', 'Network'),
    ('Application', 'Application'),
    ('Front End', 'Front End'),
    ('Deployment', 'Deployment'),
    ('Fatal', 'Fatal'),
)

assigned_to = (
    ('Group', 'Group'),
    ('Manager', 'Manager'),
)

status = (
    ('Open', 'Open'),
    ('Closed', 'Closed'),
    ('Resolved', 'Resolved'),
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
    ('Pending', 'Pending'),
    ('Fixed', 'Fixed'),
    ('Irreproducible', 'Irreproducible'),
    ('Deferred', 'Deferred'),
    ('As Designed', 'As Designed'),
    ('Cannot be fixed', 'Cannot be fixed'),
    ('Withdrawn by Reporter', 'Withdrawn by Reporter'),
    ('Need More Info', 'Need More Info'),
    ('Disagree with Suggestion', 'Disagree with Suggestion'),
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
    ('abc@bughound.com', 'abc@bughound.com'),
    ('def@bughound.com', 'def@bughound.com'),
)

tested_by = (
    ('abc@bughound.com', 'abc@bughound.com'),
    ('def@bughound.com', 'def@bughound.com'),
)


# Create your models here.
class Bugtracker(models.Model):
    program = models.CharField(max_length=20, choices=program_choices, default='vscode')
    report_type = models.CharField(max_length=20, choices=report_type, default='coding_error')
    severity = models.CharField(max_length=20, choices=severity, default='mild')
    problem_summary = models.TextField(default='summary')
    release = models.CharField(max_length=20, default='rel_01')
    version = models.CharField(max_length=20, default='1.0')
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
    attachment = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.program
