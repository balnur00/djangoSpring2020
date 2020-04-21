from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from main.models import PersonalTaskList
from main.serializers import PerTaskListSerializer

import logging
logger = logging.getLogger('api')


class PersonalTaskListViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              viewsets.GenericViewSet):
    def get_queryset(self):
        return PersonalTaskList.objects.created_by_user(self.request.user)

    def get_serializer_class(self):
        return PerTaskListSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)
        logger.info(f'Personal To-do List with id = {serializer.data["id"]} created')

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class PersonalTaskListDetailViewSet(mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.CreateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    pass


class PersonalTaskViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              viewsets.GenericViewSet):
    pass


class PersonalTaskDetailViewSet(mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.CreateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    pass