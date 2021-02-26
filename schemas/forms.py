from django.forms import ModelForm
from.models import Schema, Dataset


class SchemaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SchemaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Schema
        fields = ['name', 'column_separator_type', 'string_character_type', 'user']
