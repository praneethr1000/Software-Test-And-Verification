from django.db import models
from .employee_model import Employee
from .program_model import Program
from .area_model import Area
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
    # TODO: Update this to pull program choices from the Program database table
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL, editable=True, unique=False)
    # program = models.CharField(max_length=20, choices=program_choices, default='vscode')
    report_type = models.CharField(max_length=20, choices=report_type, null=True, blank=True)
    severity = models.CharField(max_length=20, choices=severity, null=True, blank=True)
    problem_summary = models.TextField(null=False, blank=False)
    # TODO: Make these 2 as dynamic fields to update according to the program choice
    release = models.CharField(max_length=20, null=True, blank=True)
    version = models.CharField(max_length=20, null=True, blank=True)
    # TODO: 1. Update the new field here
    problem = models.TextField(null=False, blank=False)
    suggested_fix = models.TextField(null=True, blank=True)
    reproducible = models.TextField(null=True, blank=True)
    # functional_area = models.CharField(max_length=20, choices=functional_area)
    functional_area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL, editable=True, blank=True)
    assigned_to = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, editable=True, related_name="assigned", blank=True)
    comments = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=status, default='Open')
    priority = models.CharField(max_length=100, choices=priority, null=True, blank=True)
    resolution = models.CharField(max_length=100, choices=resolution, null=True, blank=True)
    resolution_version = models.CharField(max_length=100, null=True, blank=True)
    resolved_by = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, editable=True, related_name="resolved", blank=True)
    resolved_date = models.DateField(null=True, blank=True)
    tested_by = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, editable=True, related_name="tested", blank=True)
    tested_date = models.DateField(null=True, blank=True)
    treated_as_deferred = models.TextField(null=True, blank=True)

    # reported_by = models.CharField(max_length=20, choices=reported_by)
    reported_by = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, editable=True)
    date = models.DateField(null=True, blank=True)
    id = models.AutoField(primary_key=True)
    attachment = models.FileField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return str(self.id)
