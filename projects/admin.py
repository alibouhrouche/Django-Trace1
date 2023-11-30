from django.contrib import admin

from .models import Project, Organisation, Phase


class PhaseInline(admin.StackedInline):
    model = Phase
    extra = 1


# Register your models here.
@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    search_fields = ("code", "nom")
    inlines = [PhaseInline]


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    search_fields = ("code", "nom")


@admin.register(Phase)
class PhaseAdmin(admin.ModelAdmin):
    search_fields = ("code", "nom", "project__nom")
    list_display = [
        "code",
        "nom",
        "project_name",
        "finished",
        "invoiced",
        "payed",
        "percentage",
    ]
    readonly_fields = ("project_name",)

    @admin.display(
        description="Project",
    )
    def project_name(self, obj):
        return obj.project.code + " - " + obj.project.nom
