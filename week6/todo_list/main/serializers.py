from rest_framework import serializers

from auth_.serializers import MyUserSerializer
from main.models import TaskList, Task


class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = MyUserSerializer(read_only=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by')


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_date', 'status', 'priority', 'task_list')
