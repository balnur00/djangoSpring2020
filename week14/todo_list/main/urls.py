from rest_framework.routers import DefaultRouter
from django.urls import path
from main import viewsets
from .views import BusTaskListApiView, BusTaskListDetailApiView, BusTaskApiView, BusTaskDetailApiView, ReceiverApiView

urlpatterns = [
    path('business/', BusTaskListApiView.as_view()),
    path('business/<int:pk>/', BusTaskListDetailApiView.as_view()),
    path('business/<int:pk>/tasks/', BusTaskApiView.as_view()),
    path('business/<int:pk2>/tasks/<int:pk>/', BusTaskDetailApiView.as_view()),

    path('receiver/', ReceiverApiView.as_view()),
]


router = DefaultRouter()
router.register(r'lists', viewsets.PersonalTaskListViewSet, basename='lists')


urlpatterns += router.urls
