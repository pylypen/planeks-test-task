from django.urls import path
from . import views
from .views import ListSchemaView, CreateSchemaView

urlpatterns = [
    path('', ListSchemaView.as_view(), name='schema_list'),
    path('view/<int:id>/', views.SchemaView.as_view(), name='schema_view'),
    path('create/', CreateSchemaView.as_view(), name='schema_create'),
    path('edit/<int:id>/', views.edit_schema, name='schema_edit'),
    path('column/types/', views.get_columns_types, name='schema_column_types'),
]
