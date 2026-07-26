from django.urls import path

from apps.tasks.views import TaskDetailAPIView, TaskListAPIView

urlpatterns = [
    path("update/", TaskDetailAPIView.as_view()),
    path("list/", TaskListAPIView.as_view()),
]
