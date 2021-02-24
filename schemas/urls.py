from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_schema, name='schema_list'),
    path('view/<int:id>/', views.view_schema, name='schema_view'),
    path('create/', views.create_schema, name='schema_create'),
    path('edit/<int:id>/', views.edit_schema, name='schema_edit'),
]
