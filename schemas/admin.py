from django.contrib import admin
from .models import Schema, Dataset, Column, ColumnTypes


admin.site.register(Schema)
admin.site.register(Dataset)
admin.site.register(Column)
admin.site.register(ColumnTypes)

