from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, Announcement, Event, Membership, EventRegistration
from .forms import SignupForm


def home_view(request):
    clubs = Club.objects.all().order_by('name')
    events = Event.objects.select_related('club').order_by('date', 'time')[:6]
    announcements = Announcement.objects.select_related('club').order_by('-created_at')[:5]
    return render(request, 'clubApp/home.html', {
        'clubs': clubs,
        'events': events,
        'announcements': announcements,
    })


def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('/accounts/login/')
    return render(request, 'clubApp/signup.html', {'form': form})


@login_required
def dashboard_view(request):
    memberships = Membership.objects.filter(student=request.user, active=True).select_related('club')
    registrations = EventRegistration.objects.filter(student=request.user).select_related('event', 'event__club').order_by('event__date')
    return render(request, 'clubApp/dashboard.html', {
        'memberships': memberships,
        'registrations': registrations,
    })


@login_required
def clubs_view(request):
    clubs = Club.objects.all().order_by('name')
    joined_ids = set(Membership.objects.filter(student=request.user, active=True).values_list('club_id', flat=True))
    return render(request, 'clubApp/clubs.html', {'clubs': clubs, 'joined_ids': joined_ids})


@login_required
def club_detail_view(request, id):
    club = get_object_or_404(Club, id=id)
    joined = Membership.objects.filter(student=request.user, club=club, active=True).exists()
    events = club.events.order_by('date', 'time')
    members_count = club.memberships.filter(active=True).count()
    return render(request, 'clubApp/club_detail.html', {
        'club': club,
        'joined': joined,
        'events': events,
        'members_count': members_count,
    })


@login_required
def join_club_view(request, id):
    club = get_object_or_404(Club, id=id)
    Membership.objects.get_or_create(student=request.user, club=club)
    messages.success(request, f'You joined {club.name}.')
    return redirect('club_detail', id=id)


@login_required
def events_view(request):
    events = Event.objects.select_related('club').order_by('date', 'time')
    registered_ids = set(EventRegistration.objects.filter(student=request.user).values_list('event_id', flat=True))
    return render(request, 'clubApp/events.html', {'events': events, 'registered_ids': registered_ids})


@login_required
def register_event_view(request, id):
    event = get_object_or_404(Event, id=id)
    EventRegistration.objects.get_or_create(student=request.user, event=event)
    messages.success(request, f'You registered for {event.title}.')
    return redirect('events')


@login_required
def announcements_view(request):
    announcements = Announcement.objects.select_related('club').order_by('-created_at')
    return render(request, 'clubApp/announcements.html', {'announcements': announcements})
