from django.urls import path

from .views import BusTaskListApiView, BusTaskListDetailApiView, BusTaskApiView, BusTaskDetailApiView

urlpatterns = [
    path('business/', BusTaskListApiView.as_view()),
    path('business/<int:pk>/', BusTaskListDetailApiView.as_view()),
    path('business/<int:pk>/tasks/', BusTaskApiView.as_view()),
    path('business/<int:pk2>/tasks/<int:pk>/', BusTaskDetailApiView.as_view()),
]