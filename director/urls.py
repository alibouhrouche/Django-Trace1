from django.urls import path

from .views import projects_view, edit_project_view, new_project_view

app_name = "director"
urlpatterns = [
    path("projects/", view=projects_view, name="projects"),
    path("projects/new/", view=new_project_view, name="new_project"),
    path("projects/edit/<pk>/", view=edit_project_view, name="edit_project"),
]
