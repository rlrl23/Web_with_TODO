from cProfile import label
from django_filters import rest_framework as filters
from .models import Todo


class DateCreatedFilter(filters.FilterSet):
    created = filters.DateFromToRangeFilter(
        label='Please, enter the range: created after created before')

    class Meta:
        model = Todo
        fields = ['created']
