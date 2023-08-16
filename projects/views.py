from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project, Tag
from .forms import Projectform
from .utils import searchProject, paginate_project



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
    projects, search_query = searchProject(request)
    custom_range, projects = paginate_project(request, projects, 4)


    context = {'projects': projects, 'search_query': search_query,
             'custom_range': custom_range}
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
    profile = request.user.profile
    form = Projectform()
    if request.method == 'POST':
        # print(request.POST)
        form = Projectform(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
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
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_object.html', context)