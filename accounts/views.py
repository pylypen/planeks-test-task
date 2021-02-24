from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.method == 'POST':
        return redirect('schema_list')

    return render(request, 'accounts/login.html')
