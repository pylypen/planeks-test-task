from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from schemas.models import Schema


@login_required
@csrf_exempt
def list_schema(request):
    return render(request, 'schemas/list.html', {
        "schemas": Schema.objects.all()
    })


@login_required
@csrf_exempt
def create_schema(request):
    return render(request, 'schemas/create.html')


@login_required
@csrf_exempt
def edit_schema(request, id):
    return render(request, 'schemas/edit.html')


@login_required
@csrf_exempt
def view_schema(request, id):
    return render(request, 'schemas/view.html')
