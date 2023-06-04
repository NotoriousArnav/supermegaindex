import django_filters
from index.models import Record

class RecordFilter(django_filters.FilterSet):
    # Define filters for your model fields
    title = django_filters.CharFilter(lookup_expr='icontains')
    # Add more filters as needed

    class Meta:
        model = Record
        fields = ['title', 'date_uploaded', 'user', 'description', 'link']  # Add more fields as needed
