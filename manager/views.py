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


def save_team(phase, request):
    phase.team.clear()
    for t in request.POST.getlist('team'):
        u = User.objects.get(username=t)
        phase.team.add(u)


def save_phase(phase, request):
    phase.nom = request.POST.get('nom')
    phase.description = request.POST.get('description')
    phase.start_date = request.POST.get('start_date')
    phase.end_date = request.POST.get('end_date')
    phase.percentage = request.POST.get('percentage')
    phase.finished = request.POST.get('finished', 'off') == 'on'
    save_team(phase, request)
    phase.save()


def new_phase_view(request, pk):
    if request.user.is_authenticated:
        user = request.user  # type: User
        if user.is_chief():
            project = user.directed_projects.get(pk=pk)
            if request.method == 'GET':
                return render(request, 'manager/new_phase.html', {
                    'members': User.objects.all(),
                    'project': project,
                })
            phase = project.phases.create(
                code=request.POST.get('code'),
                nom=request.POST.get('nom'),
                description=request.POST.get('description'),
                start_date=request.POST.get('start_date'),
                end_date=request.POST.get('end_date'),
                percentage=request.POST.get('percentage'),
                invoiced=False,
                finished=request.POST.get('finished', 'off') == 'on',
                payed=False,
            )
            save_team(phase, request)
            phase.save()
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
