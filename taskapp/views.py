from django.shortcuts import render, redirect
from .models import *
from .forms import *

 
def index(request):
    tasks = Task.objects.all()
    
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {
        'task':tasks,
        'form':form, 
    }
    return render(request,'taskapp/list.html',context)

def update_task(request,pk):
    tasks = Task.objects.get(id=pk)

    form = TaskForm(instance=tasks)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {
        'form': form
    }

    return render(request,'taskapp/update_task.html',context)

def delete_task(request,pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return redirect('/')