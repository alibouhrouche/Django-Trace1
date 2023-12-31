from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from accounts.models import User
from projects.models import Project, Organisation


def projects_view(request):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_superuser or user.is_director():
            return render(request, 'director/projects.html', {
                'projects': Project.objects.all(),
            })
    raise PermissionDenied


def save_project(project, request):
    project.nom = request.POST['nom']
    project.budget = request.POST['budget']
    project.chief = User.objects.get(username=request.POST['chief'])
    project.description = request.POST['description']
    project.client = Organisation.objects.get(code=request.POST['client'])
    project.start_date = request.POST['start_date']
    project.end_date = request.POST['end_date']
    project.save()


def new_project_view(request):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_superuser or user.is_director():
            if request.method == 'GET':
                return render(request, 'director/new_project.html', {
                    'organisations': Organisation.objects.all(),
                    'chiefs': [x for x in User.objects.all() if x.is_chief()],
                })
            project = Project()
            project.code = request.POST['code']
            save_project(project, request)
            return render(request, 'director/project_row.html', {
                'project': project,
            })
    raise PermissionDenied


def edit_project_view(request, pk):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_superuser or user.is_director():
            if request.method == 'GET':
                return render(request, 'director/edit_project.html', {
                    'project': Project.objects.get(pk=pk),
                    'organisations': Organisation.objects.all(),
                    'chiefs': [x for x in User.objects.all() if x.is_chief()],
                })
            project = Project.objects.get(pk=pk)
            save_project(project, request)
            return render(request, 'director/project_row.html', {
                'project': project,
            })
    raise PermissionDenied


def delete_project_view(request, pk):
    if request.method != 'DELETE':
        return HttpResponse(status=405)
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_superuser or user.is_director():
            project = Project.objects.get(pk=pk)
            project.delete()
            return HttpResponse(status=200, content="")
    raise PermissionDenied
