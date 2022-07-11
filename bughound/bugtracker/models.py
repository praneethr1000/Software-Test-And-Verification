from django.db import models


# Create your models here.
class Bugtracker(models.Model):
    program = models.CharField(max_length=200)
    report_type = models.CharField(max_length=200)
    severity = models.CharField(max_length=20)
    problem_summary = models.TextField()
    reported_by = models.CharField(max_length=200)
    date = models.DateField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.program
