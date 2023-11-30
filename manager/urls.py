from django.urls import path

from . import views

app_name = 'manager'
urlpatterns = [
    path('projects/', views.projects_view, name='projects'),
    path('projects/<pk>/phases', views.phases_view, name='phases'),
    path('projects/<pk>/phases/new', views.new_phase_view, name='new_phase'),
    path('projects/<pk>/phases/<phase_pk>/edit', views.edit_phase_view, name='edit_phase'),
]
