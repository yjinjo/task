from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from taskapp.forms import TaskForm
from taskapp.models import Task


def index(request):
    context = {}
    return render(request, "pages/index.html", context)


class TaskListView(TemplateView):
    template_name = "pages/task_list.html"

    def get_context_data(self, **kwargs):
        tasks = Task.objects.all()

        return {"tasks": tasks}


class TaskCreateView(FormView):
    template_name = "pages/task_create.html"
    form_class = TaskForm
    success_url = "/"

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
