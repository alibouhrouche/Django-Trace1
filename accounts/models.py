from django.contrib.auth.models import AbstractUser
from django.db import models
from hashlib import sha256


class User(AbstractUser):
    PROFILES = (
        ('TH', 'Technician'),
        ('SE', 'Secretary'),
        ('CP', 'Project Chief'),
        ('IG', 'Engineer'),
        ('DR', 'Director'),
        ('FN', 'Finance'),
        ('NA', 'Other'),
    )
    telephone = models.CharField(max_length=11, unique=True, null=True)
    number = models.CharField(max_length=20, unique=True, null=True)
    profile = models.CharField(max_length=2, choices=PROFILES, default='NA')

    def is_secretary(self):
        return self.profile == 'SE'

    def is_director(self):
        return self.profile == 'DR'

    def is_chief(self):
        return self.profile == 'CP'

    def full_profile(self):
        if self.is_superuser:
            return "Superuser"
        return [x for x in self.PROFILES if x[0] == self.profile][0][1]

    def can_manage_projects(self):
        return (self.profile == 'DR') or (self.profile == 'CP') or (self.profile == 'SE') or self.is_superuser

    def can_manage_clients(self):
        return (self.profile == 'SE') or self.is_superuser

    def can_manage_invoices(self):
        return (self.profile == 'FN') or self.is_superuser

    def get_avatar(self):
        return "https://gravatar.com/avatar/"+sha256(self.email.strip().lower().encode()).hexdigest() + "?d=identicon"
