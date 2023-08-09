from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import Projectform


# Create your views here.
# projectslist = [
#     {
#         'id': '1',
#         'title': "Ecommerce Website",
#         'description': "fully functional ecommerce website"
#     },
#     {
#         'id': '2',
#         'title': "Portfolio website",
#         'description': "fully functional ecommerce website"
#     },
#     {
#         'id': '3',
#         'title': "Social Network",
#         'description': "awesome functional ecommerce website"
#     }

# ]
# @login_required(login_url='login')
def projects(request):
    # msg = 'hello, you are on the projects page'
    # page = 'projects_hmmm'
    # number = 11
    projects = Project.objects.all()
    context = {'projects': projects}
    # context = {'page': page, 'number':number, 'projects':projectslist}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    print('projectObj:', projectObj)

    # projectObj = None
    # for i in projectslist:
    #     if i['id'] == pk:
    #         projectObj = i

    return render(request, 'projects/single-project.html', {'project': projectObj, 'tags': tags})
@login_required(login_url='login')
def create_project(request):
    form = Projectform()
    if request.method == 'POST':
        # print(request.POST)
        form = Projectform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = Projectform(instance=project)
    if request.method == 'POST':
        form = Projectform(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def deleteproject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_object.html', context)