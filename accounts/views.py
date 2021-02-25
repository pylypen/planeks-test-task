from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import messages, auth


@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect('schema_list')

    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('schema_list')
        else:
            messages.error(request, 'Incorrect username or password')

    return render(request, 'accounts/login.html')


@csrf_exempt
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, 'Logout done')

    return redirect('login')
