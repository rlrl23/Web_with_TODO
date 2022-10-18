import graphene
from graphene_django import DjangoObjectType
from mainapp.models import Project, Todo
from authapp.models import User


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    todo_of_project = graphene.List(
        TodoType, project_id=graphene.Int(required=True))
    project_by_name = graphene.Field(
        ProjectType, name=graphene.String(required=True))
    users_by_post = graphene.List(
        UserType, post=graphene.String(required=True))

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_todo_of_project(root, info, project_id):
        todo = Todo.objects.all()
        try:
            return todo.filter(project=project_id)
        except Todo.DoesNotExist:
            return None

    def resolve_project_by_name(root, info, name):
        try:
            return Project.objects.get(name=name)
        except Project.DoesNotExist:
            return None

    def resolve_users_by_post(root, info, post):
        try:
            return User.objects.all().filter(is_staff=post)
        except User.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
