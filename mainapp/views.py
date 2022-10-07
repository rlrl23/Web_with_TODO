from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from mainapp.models import Project, Todo
from mainapp.serializers import ProjectModelSerializer, TodoModelSerializer
from rest_framework import filters
from rest_framework.response import Response
from .filters import DateCreatedFilter
from rest_framework.permissions import IsAuthenticated


class ProjectPageNumberPagination(PageNumberPagination):
    page_size = 10


class TodoPageNumberPagination(PageNumberPagination):
    page_size = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class TodoModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoPageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['project__name']
    filterset_class = DateCreatedFilter

    def destroy(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        todo.active = False
        todo.save()
        return Response(request.data)
