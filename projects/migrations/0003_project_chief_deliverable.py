# Generated by Django 4.1 on 2023-11-29 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_rename_projects_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='chief',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='deliverables')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliverables', to='projects.phase')),
            ],
        ),
    ]