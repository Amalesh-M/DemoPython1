
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class tasklv(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'Task1'

class Taskdv(DetailView):
    model = task
    template_name = 'new.html'
    context_object_name = 'Task2'

class Taskupdatev(UpdateView):
    model = task
    template_name = 'updates.html'
    context_object_name = 'Task4'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})

class taskdeletev(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



# Create your views here.
def add(request):
    Task1 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task', '')
        priority=request.POST.get('priority', '')
        date=request.POST.get('date', '')
        Task=task(name=name, priority=priority, date=date)
        Task.save()
    return render(request, "home.html", {'task1': Task1})

# def details(request):
#
#     return render(request, 'details.html', )

def delete(request,taskid):
    Task=task.objects.get(id=taskid)
    if request.method =='POST':
        Task.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request,id):
    Task=task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=Task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'Task': Task})
