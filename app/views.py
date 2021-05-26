from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Tasks


# Create your views here.
def index(request):
    showTasks = Tasks.objects.all()
    context = {
        'tasks': showTasks,
        'fields_name': Tasks._meta.fields,
    }
    if request.method == 'POST':
        name = request.POST.get('task')
        description = request.POST.get('description')
        task = Tasks(task_name=name, desc_task=description)
        task.save()

        # print(f'task: {name}\ndescription:{description}')
        return redirect('/')
    else:
        return render(request, 'index.html', context)