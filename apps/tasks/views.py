from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


class CreateTask(CreateAPIView):

    serializer_class = TaskSerializer
    permission_classes = IsAuthenticated

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskDetailAPIView(
    RetrieveUpdateDestroyAPIView
):

    serializer_class = TaskSerializer

    permission_classes = IsAuthenticated

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)