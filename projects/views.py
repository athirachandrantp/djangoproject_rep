from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.
projectslist = [
    {
        'id': '1',
        'title': "Ecommerce Website",
        'description': "fully functional ecommerce website"
    },
    {
        'id': '2',
        'title': "Portfolio website",
        'description': "fully functional ecommerce website"
    },
    {
        'id': '3',
        'title': "Social Network",
        'description': "awesome functional ecommerce website"
    }

]
def projects(request):
    # msg = 'hello, you are on the projects page'
    # page = 'projects_hmmm'
    # number = 11
    projects = Project.objects.all()
    context = {'projects': projects}
    # context = {'page': page, 'number':number, 'projects':projectslist}
    return render(request, 'projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    print('projectObj:', projectObj)

    # projectObj = None
    # for i in projectslist:
    #     if i['id'] == pk:
    #         projectObj = i

    return render(request, 'single-project.html', {'project': projectObj, 'tags': tags})
