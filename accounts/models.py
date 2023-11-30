from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telephone = models.CharField(max_length=11, unique=True, null=True)
    number = models.CharField(max_length=20, unique=True, null=True)
    profile = models.CharField(max_length=2, choices=(
        ('TH', 'Technician'),
        ('SE', 'Secretary'),
        ('CP', 'Project Chief'),
        ('IG', 'Engineer'),
        ('DR', 'Director'),
        ('FN', 'Finance'),
        ('NA', 'Other'),
    ), default='NA')

    def is_secretary(self):
        return self.profile == 'SE'

    def is_director(self):
        return self.profile == 'DR'

    def is_chief(self):
        return self.profile == 'CP'

    def can_manage_projects(self):
        return (self.profile == 'DR') or (self.profile == 'CP') or (self.profile == 'SE') or self.is_superuser

    def can_manage_clients(self):
        return (self.profile == 'SE') or self.is_superuser

    def can_manage_invoices(self):
        return (self.profile == 'FN') or self.is_superuser
