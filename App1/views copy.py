from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Task
# from django.template import loader
from django.urls import reverse_lazy

# Create your views here.
# def testRequest(request):
#     return HttpResponse('first.html')

# def testRequest(request):
#     return HttpResponse(loader.get_template('first.html').render())


def testRequest(request):
    return HttpResponse(render(request,'first.html'))

class PendingList(ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "App1/task.html"

class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
