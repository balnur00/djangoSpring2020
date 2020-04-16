from django.urls import path

from .views import TaskListApiView, TaskListDetailApiView, TaskApiView, TaskDetailApiView

urlpatterns = [
    path('', TaskListApiView.as_view()),
    path('<int:pk>/', TaskListDetailApiView.as_view()),
    path('<int:pk>/tasks/', TaskApiView.as_view()),
    path('<int:pk2>/tasks/<int:pk>/', TaskDetailApiView.as_view()),
]