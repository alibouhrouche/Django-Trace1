from django.db import models

from accounts.models import User


class Organisation(models.Model):
    code = models.CharField(max_length=20, unique=True, primary_key=True)
    nom = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)


# Create your models here.
class Project(models.Model):
    code = models.CharField(max_length=20, unique=True, primary_key=True)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    client = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        related_name="projects",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()
    chief = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="directed_projects",
        null=True,
    )


class Phase(models.Model):
    code = models.CharField(max_length=20, unique=True, primary_key=True)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="phases",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    team = models.ManyToManyField(
        User,
        related_name="phases",
    )
    percentage = models.IntegerField()
    finished = models.BooleanField()
    invoiced = models.BooleanField()
    payed = models.BooleanField()
    

class Deliverable(models.Model):
    code = models.CharField(max_length=20, unique=True, primary_key=True)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    phase = models.ForeignKey(
        Phase,
        on_delete=models.CASCADE,
        related_name="deliverables",
    )
    file = models.FileField(upload_to="deliverables")
