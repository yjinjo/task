from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, ListView

from taskapp.models import Task


def index(request):
    context = {}
    return render(request, "pages/index.html", context)


class TaskListView(TemplateView):
    template_name = "pages/task_list.html"

    def get_context_data(self, **kwargs):
        tasks = Task.objects.filter(due__gte=timezone.now()).order_by("-due")

        return {"tasks": tasks}


class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "type", "due"]
    template_name = "pages/task_create.html"
    success_url = "/"


class TaskPreviousListView(ListView):
    """Due Date 이 지난 Task 들을 보여주는 클래스"""

    model = Task
    template_name = "pages/task_previous_list.html"
    queryset = Task.objects.filter(due__lt=timezone.now()).order_by("-due")
