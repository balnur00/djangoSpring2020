from django.contrib.auth import logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json


@csrf_exempt
def login_view(request):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        # return HttpResponseRedirect("/account/loggedin/")
        return JsonResponse({'status': 'logged in'}, status=200)
    else:
        # return HttpResponseRedirect("/account/invalid/")
        return JsonResponse({'status': 'logged out'}, status=200)


@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/account/loggedout/")