from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def list_schema(request):
    return render(request, 'schemas/list.html')


@csrf_exempt
def create_schema(request):
    return render(request, 'schemas/create.html')


@csrf_exempt
def edit_schema(request, id):
    return render(request, 'schemas/edit.html')


@csrf_exempt
def view_schema(request, id):
    return render(request, 'schemas/view.html')
