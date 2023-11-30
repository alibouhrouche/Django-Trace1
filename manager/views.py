from django.shortcuts import render
from accounts.models import User


# Create your views here.
def projects_view(request):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_chief():
            return render(request, 'manager/projects.html', {
                'projects': user.directed_projects.all(),
            })
    raise PermissionError


def phases_view(request, pk):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_chief():
            project = user.directed_projects.get(pk=pk)
            return render(request, 'manager/phases.html', {
                'phases': project.phases.all(),
                'project': project,
            })
    raise PermissionError


def save_phase(phase, request):
    phase.nom = request.POST.get('nom')
    phase.budget = request.POST.get('budget')
    phase.team.clear()
    for t in request.POST.getlist('team'):
        u = User.objects.get(username=t)
        phase.team.add(u)
    try:
        phase.finished = request.POST.get('finished') == 'on'
    except KeyError:
        phase.finished = False
    phase.save()


def new_phase_view(request, pk):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_chief():
            project = user.directed_projects.get(pk=pk)
            if request.method == 'GET':
                return render(request, 'manager/new_phase.html', {
                    'project': project,
                })
            phase = project.phases.create()
            save_phase(phase, request)
            return render(request, 'manager/phase_row.html', {
                    'phase': phase,
                    'project': project,
            })
    raise PermissionError


def edit_phase_view(request, pk, phase_pk):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_chief():
            phase = user.directed_projects.get(pk=pk).phases.get(pk=phase_pk)
            if request.method == 'GET':
                return render(request, 'manager/edit_phase.html', {
                    'phase': phase,
                    'project': phase.project,
                    'team': [x.username for x in phase.team.all()],
                    'members': User.objects.all(),
                })
            save_phase(phase, request)
            return render(request, 'manager/phase_row.html', {
                    'phase': phase,
                    'project': phase.project,
            })
    raise PermissionError
