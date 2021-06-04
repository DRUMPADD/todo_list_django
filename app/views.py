from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .models import Tasks
from .forms import signUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login/')
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

def register(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')
    else:
        form = signUpForm()
    return render(request, 'auth/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            return redirect('/')
    form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def updateTask(request):
    if request.method == 'POST':
        idT = request.POST['idT']
        nameT = request.POST['task']
        descT = request.POST['description']
        task = Tasks.objects.get(id_task = idT)
        task.task_name = nameT
        task.desc_task = descT
        task.save()
    return redirect('/')

def deleteTask(request, id):
    task = Tasks.objects.get(id_task=id)
    task.delete()
    return redirect('/')