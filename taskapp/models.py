from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    class TaskType(models.TextChoices):
        JOB = "JOB", _("업무")
        HEALTH = "HEALTH", _("건강")
        SOCIAL = "SOCIAL", _("사회")

    title = models.CharField(max_length=50, null=False)
    type = models.CharField(
        choices=TaskType.choices, max_length=10, default=TaskType.JOB
    )
    due = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class ChecklistItem(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, null=False)
    checked = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
