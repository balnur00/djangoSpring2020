from rest_framework import serializers

from auth_.serializers import MyUserSerializer
from main.models import BusinessTaskList, PersonalTaskList, BusinessTask, PersonalTask, Receiver


class PerTaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = MyUserSerializer(read_only=True)

    class Meta:
        model = PersonalTaskList
        fields = ('id', 'title', 'created_by')


class BusTaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = MyUserSerializer(read_only=True)

    class Meta:
        model = BusinessTaskList
        fields = ('id', 'title', 'created_by', 'image')


class BusTaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BusinessTask
        fields = ('id', 'name', 'created_at', 'due_date', 'status', 'priority', 'task_list')


class PerTaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = PersonalTask
        fields = ('id', 'name', 'created_at', 'status', 'task_list', 'image')


class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ('desc', )

