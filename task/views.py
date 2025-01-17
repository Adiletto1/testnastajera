from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class TaskListApiView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
