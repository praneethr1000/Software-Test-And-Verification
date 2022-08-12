from django.db import models

levels = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
)


class Employee(models.Model):
    user = models.TextField(max_length=100, unique=True, null=False, blank=False)
    loginID = models.TextField(max_length=100, unique=True, null=False, blank=False)
    level = models.CharField(max_length=20, choices=levels, default='1')

    def __str__(self):
        return str(self.user)