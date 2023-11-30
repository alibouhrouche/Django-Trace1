from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from accounts.models import User
from projects.models import Project, Organisation


def projects_view(request):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_superuser or user.is_secretary():
            return render(request, 'secretary/projects.html', {
                'projects': Project.objects.order_by('-start_date'),
            })
    raise PermissionDenied


def save_project(project, request):
    project.nom = request.POST['nom']
    project.description = request.POST['description']
    project.client = Organisation.objects.get(code=request.POST['client'])
    project.start_date = request.POST['start_date']
    project.end_date = request.POST['end_date']
    project.save()


def new_project_view(request):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_superuser or user.is_secretary():
            if request.method == 'GET':
                return render(request, 'secretary/new_project.html', {
                    'organisations': Organisation.objects.all(),
                })
            project = Project()
            project.code = request.POST['code']
            project.budget = 0
            save_project(project, request)
            return render(request, 'secretary/project_row.html', {
                'project': project,
            })
    raise PermissionDenied


def edit_project_view(request, pk):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_superuser or user.is_secretary():
            if request.method == 'GET':
                return render(request, 'secretary/edit_project.html', {
                    'project': Project.objects.get(pk=pk),
                    'organisations': Organisation.objects.all(),
                })
            project = Project.objects.get(pk=pk)
            save_project(project, request)
            return render(request, 'secretary/project_row.html', {
                'project': project,
            })
    raise PermissionDenied


def clients_view(request):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_superuser or user.is_secretary():
            return render(request, 'secretary/clients.html', {
                'organisations': Organisation.objects.all(),
            })
    raise PermissionDenied


def save_client(organisation, request):
    organisation.nom = request.POST['nom']
    organisation.address = request.POST['address']
    organisation.telephone = request.POST['telephone']
    organisation.contact_name = request.POST['contact_name']
    organisation.contact_email = request.POST['contact_email']
    organisation.website = request.POST['website']
    organisation.save()


def new_client_view(request):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_superuser or user.is_secretary():
            if request.method == 'GET':
                return render(request, 'secretary/new_client.html', {})
            organisation = Organisation()
            organisation.code = request.POST['code']
            save_client(organisation, request)
            return render(request, 'secretary/client_row.html', {
                'client': organisation,
            })
    raise PermissionDenied


def edit_client_view(request, pk):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_superuser or user.is_secretary():
            if request.method == 'GET':
                return render(request, 'secretary/edit_client.html', {
                    'client': Organisation.objects.get(pk=pk),
                })
            organisation = Organisation.objects.get(pk=pk)
            save_client(organisation, request)
            return render(request, 'secretary/client_row.html', {
                'client': organisation,
            })
    raise PermissionDenied
