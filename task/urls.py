from django.urls import path
from .views import TaskListApiView, TaskDetail

urlpatterns = [
    path('api/v1/tasklist/', TaskListApiView.as_view()),
    path('api/v1/tasklist/<int:id>/', TaskDetail.as_view())
]