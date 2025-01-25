from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.utils import timezone
from .models import User, Message
from .forms import MessageForm, UserCreationForm
from django.db.models import Q  
from django.contrib.auth.decorators import user_passes_test
import random
import string
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from django.contrib import messages as django_messages

def home(request):
    current_year = timezone.now().year
    if not request.user.is_authenticated and 'logged_out' in request.session:
        django_messages.success(request, 'You have been successfully logged out.')
        del request.session['logged_out']
    return render(request, 'home.html', {'year': current_year})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def send_message_to_eb(request):
    eb_users = User.objects.filter(is_superuser=True)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message_content = form.cleaned_data['content']
            for eb_user in eb_users:
                Message.objects.create(
                    sender=request.user,
                    receiver=eb_user,
                    content=message_content
                )
            return redirect('dashboard')
    else:
        form = MessageForm()
    
    return render(request, 'send_message.html', {
        'form': form,
        'is_eb_message': True  
    })


@login_required
def send_message_to_nation(request):
    active_cutoff = timezone.now() - timedelta(minutes=settings.USER_ACTIVITY_TIMEOUT)
    
    active_nations = User.objects.filter(
        last_activity__gte=active_cutoff,
        is_eb=False,
        is_active=True
    ).exclude(id=request.user.id)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = User.objects.get(id=request.POST.get('receiver'))
            message.save()
            return redirect('dashboard')
    else:
        form = MessageForm()
    
    return render(request, 'send_message.html', {
        'form': form,
        'receivers': active_nations,
        'active_cutoff': active_cutoff,
    })

@login_required
def messages(request):
    user_messages = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by('-timestamp')
    
    Message.objects.filter(
        receiver=request.user,
        is_read=False
    ).update(is_read=True)
    
    return render(request, 'messages.html', {
        'messages': user_messages
    })


@login_required
def notifications(request):
    unread_count = Message.objects.filter(
        receiver=request.user,
        is_read=False
    ).count()
    return JsonResponse({'count': unread_count})

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def user_management(request):
    users = User.objects.all().order_by('country')
    return render(request, 'user_management.html', {'users': users})

@user_passes_test(is_superuser)
def generate_credentials(request):
    users = User.objects.all().order_by('country')
    
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="credentials.txt"'
    
    for user in users:
        response.write(f"Country: {user.country}\n")
        response.write(f"Username: {user.username}\n")
        response.write(f"Password: {user.username}@mun2023\n")  # You might want to use a more secure way to store/retrieve passwords
        response.write("\n-------------------\n\n")
    
    return response