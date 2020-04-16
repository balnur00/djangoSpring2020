from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from rest_framework.permissions import IsAuthenticated

from main.models import TaskList, Task
from main.serializers import TaskListSerializer, TaskSerializer


class TaskListApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TaskList.objects.created_by_user(self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)


class TaskListDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TaskList.objects.created_by_user(self.request.user).filter(id=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return TaskListSerializer


class TaskApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.filter(task_list=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return TaskSerializer

    def perform_create(self, serializer):
        task_list_id = self.kwargs.get('pk')
        serializer.save(task_list=TaskList.objects.get(id=task_list_id))


class TaskDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.filter(id=self.kwargs.get('pk'), task_list=self.kwargs.get('pk2'))

    def get_serializer_class(self):
        return TaskSerializer
