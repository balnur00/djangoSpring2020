from django.contrib.auth import logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.utils import json

from auth_.models import MyUser
from auth_.serializers import MyUserSerializer


class Register(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return MyUserSerializer
