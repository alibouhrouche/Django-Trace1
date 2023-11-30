from django.urls import path

from .views import projects_view, edit_project_view, new_project_view, clients_view, edit_client_view, new_client_view

app_name = "secretary"
urlpatterns = [
    path("projects/", view=projects_view, name="projects"),
    path("projects/new/", view=new_project_view, name="new_project"),
    path("projects/edit/<pk>/", view=edit_project_view, name="edit_project"),
    path("clients/", view=clients_view, name="clients"),
    path("clients/new/", view=new_client_view, name="new_client"),
    path("clients/edit/<pk>/", view=edit_client_view, name="edit_client"),
]
