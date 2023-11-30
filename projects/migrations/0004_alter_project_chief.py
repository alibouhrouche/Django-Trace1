# Generated by Django 4.1 on 2023-11-29 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_project_chief_deliverable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='chief',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directed_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
