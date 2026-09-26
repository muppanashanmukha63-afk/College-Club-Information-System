from django.contrib import admin
from .models import Club, Announcement, Event, Membership, EventRegistration

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty_coordinator', 'student_coordinator', 'contact_email')
    search_fields = ('name', 'faculty_coordinator', 'student_coordinator')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'created_at')
    list_filter = ('club',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'date', 'time', 'venue')
    list_filter = ('club', 'date')
    search_fields = ('title', 'description')

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('student', 'club', 'role', 'active', 'joined_date')
    list_filter = ('club', 'role', 'active')

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'event', 'registered_at')
    list_filter = ('event',)
