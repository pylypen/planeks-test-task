import json

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Schema, Dataset, ColumnTypes
from .forms import SchemaForm
from django.views.generic import View, TemplateView


@method_decorator(login_required, name='dispatch')
class ListSchemaView(TemplateView):
    template_name = "schemas/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schemas'] = Schema.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class CreateSchemaView(View):
    def get(self, request):
        form = SchemaForm()

        return render(request, 'schemas/create.html', {
            "form": form
        })

    def post(self, request):
        updated_data = request.POST.copy()
        updated_data.update({'user': request.user})

        form = SchemaForm(updated_data)
        # check whether it's valid:
        print(form.errors)
        if form.is_valid():

            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return redirect('schema_list')

        return render(request, 'schemas/create.html', {
            "form": form
        })


@method_decorator(login_required, name='dispatch')
class SchemaView(View):
    def get(self, request, id):
        schema = Schema.objects.get(pk=id)
        datasets = Dataset.objects.filter(schema=schema).all()

        return render(request, 'schemas/view.html', {
            "datasets": datasets,
            'id': id
        })

    def post(self, request, id):
        schema = Schema.objects.get(pk=id)
        dataset = Dataset(schema=schema)
        dataset.save()

        return redirect('schema_view', id)


@csrf_exempt
def get_columns_types(request):
    types = ColumnTypes.objects.all()
    data = serialize("json", types, fields=('id', 'name'))

    return JsonResponse(json.loads(data), safe=False)


@login_required
@csrf_exempt
def edit_schema(request, id):
    return render(request, 'schemas/edit.html')
