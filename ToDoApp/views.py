from django.shortcuts import render ,redirect
from .models import Task
from .forms import *

# Create your views her
def index(request):
    tasks = Task.objects.all()
    total = Task.objects.all().count()

    form = TaskForm()
    if request.method=="POST":
        form= TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks': tasks, 'form':form, 'total':total}
    return render (request, 'index.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')


    context= {"form":form}

    return render(request,'update_task.html', context)


def deletetask(request, pk):
    item=Task.objects.get(id=pk)
  

    if request.method =="POST":
        item.delete()
        return redirect('/')
    
    context= {'item':item}

    return render(request, 'delete.html', context)