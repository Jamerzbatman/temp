from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    # Check if the user is a superuser
    is_superuser = request.user.is_superuser

    # Choose the base template based on the user's superuser status
    base_template = 'base/superuserBase.html' if is_superuser else 'base/userBase.html'

    # Pass the base template to the context
    context = {
        'base_template': base_template
    }

    return render(request, 'dashboard/home.html', context)