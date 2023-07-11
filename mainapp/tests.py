from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from authapp import models
from .models import Project, Todo
from .views import ProjectModelViewSet
from mixer.backend.django import mixer
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase, APIClient
from django.test import TestCase, Client
from rest_framework import status
from requests import delete
from django.urls import reverse
from django.test import TestCase
from urllib import response
import json
import pytest_django


class TestProjectsViewSet(TestCase):

    def setUp(self):
        self.user = models.User.objects.create_superuser(
            username='admin123', email='admin@admin.ru', password='admin123')
        self.user.save()

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_unauth(self):
        factory = APIRequestFactory()
        request = factory.post('/api/projects/', {'name': 'Сarsharing',
                                                  'users': [1, 2]}, format='json')
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_auth(self):
        factory = APIRequestFactory()
        request = factory.post(
            '/api/projects/',
            {'name': 'Сarsharing', 'link': 'cars@cars.com', 'users': [self.user.id]}, format='json')

        force_authenticate(request, self.user)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_admin(self):
        project = mixer.blend(Project)
        client = APIClient()
        client.login(username='admin123', password='admin123')
        response = client.put(f'/api/projects/{project.id}/',
                              {'name': 'Сarsharing', 'link': 'cars@cars.com', 'users': [self.user.id]},)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()


class TestProjectsApiSet(APITestCase):

    def setUp(self):
        self.user = models.User.objects.create_superuser(
            username='admin123', email='admin@admin.ru', password='admin123')
        self.user.save()
        self.project = mixer.blend(Project)
        self.project.save()
        self.todo = mixer.blend(Todo)
        self.todo.save()
        self.client.login(username='admin123', password='admin123')

    def test_get_project(self):

        response = self.client.get(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_token(self):
        user_token = Token.objects.create(user=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + user_token.key)
        # self.client.login(username='admin123', password='admin123')
        response = self.client.patch(
            f'/api/projects/{self.project.id}/', {'name': 'Руслан и Людмила'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=self.project.id)
        self.assertEqual(project.name, 'Руслан и Людмила')

    def test_delete_admin(self):
        self.client.login(username='admin123', password='admin123')
        response = self.client.delete(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_patch_admin(self):
        response = self.client.patch(
            f'/api/projects/{self.project.id}/', {'name': 'Sport_cars'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=self.project.id)
        self.assertEqual(project.name, 'Sport_cars')

    def test_delete_todo_admin(self):
        #todo = Todo.objects.create(project=self.project, text='bla bla', user=self.user, active=True)
        self.client.login(username='admin123', password='admin123')
        response = self.client.delete(f'/api/todo/{self.todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = Todo.objects.get(id=self.todo.id)
        self.assertFalse(todo.active)

    def test_post_todo_admin(self):
        self.client.login(username='admin123', password='admin123')
        response = self.client.post(
            f'/api/todo/', {'text': 'create a new platform', 'project': self.project.id, 'user': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
