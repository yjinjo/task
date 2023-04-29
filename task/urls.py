from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from taskapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("previous/", views.index, name="previous"),
    path("task/", views.index, name="create-task"),
    path("task/<int:task_id>/delete/", views.index, name="delete-task"),
    path("task/<int:task_id>/item/", views.index, name="create-item"),
    path("task/<int:task_id>/item/<int:check_id>/", views.index, name="check-item"),
    path(
        "task/<int:task_id>/item/<int:check_id>/delete", views.index, name="delete-item"
    ),
    path("task/<int:task_id>/", views.index, name="view-task"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
