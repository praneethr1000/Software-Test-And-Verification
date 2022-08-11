from django.db import models


class Program(models.Model):
    name = models.TextField(primary_key=True, unique=True, null=False, blank=False)
    release = models.TextField()
    version = models.TextField()
    # bug_number = models.ForeignKey(Bugtracker, default=1, on_delete=models.CASCADE)
    # area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
