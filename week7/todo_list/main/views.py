from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from rest_framework.permissions import IsAuthenticated

from main.models import BusinessTaskList, PersonalTaskList, BusinessTask, PersonalTask
from main.serializers import BusTaskListSerializer, BusTaskSerializer, PerTaskListSerializer, PerTaskSerializer


class BusTaskListApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return BusinessTaskList.objects.created_by_user(self.request.user)

    def get_serializer_class(self):
        return BusTaskListSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)


class BusTaskListDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return BusinessTask.objects.created_by_user(self.request.user).filter(id=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return BusTaskSerializer


class BusTaskApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return BusinessTask.objects.filter(task_list=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return BusTaskSerializer

    def perform_create(self, serializer):
        task_list_id = self.kwargs.get('pk')
        serializer.save(task_list=BusinessTaskList.objects.get(id=task_list_id))


class BusTaskDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return BusinessTask.objects.filter(id=self.kwargs.get('pk'), task_list=self.kwargs.get('pk2'))

    def get_serializer_class(self):
        return BusTaskSerializer
