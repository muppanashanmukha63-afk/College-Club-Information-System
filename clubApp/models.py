from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    upcoming_events = models.TextField(default="")
    conducted_events = models.TextField(default="")
    faculty_coordinator = models.CharField(max_length=150, blank=True)
    student_coordinator = models.CharField(max_length=150, blank=True)
    contact_email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True, related_name="announcements")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True, related_name="events")
    time = models.TimeField(null=True, blank=True)
    venue = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Membership(models.Model):
    ROLE_CHOICES = [
        ("Member", "Member"),
        ("Coordinator", "Coordinator"),
        ("President", "President"),
        ("Secretary", "Secretary"),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="club_memberships")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default="Member")
    joined_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["student", "club"], name="unique_student_club_membership")
        ]

    def __str__(self):
        return f"{self.student.username} - {self.club.name}"


class EventRegistration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_registrations")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["student", "event"], name="unique_student_event_registration")
        ]

    def __str__(self):
        return f"{self.student.username} - {self.event.title}"
