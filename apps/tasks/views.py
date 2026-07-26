from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated

from apps.common.utils import api_response
from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer


class CreateTask(CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class TaskListAPIView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return api_response(serializer.data)
