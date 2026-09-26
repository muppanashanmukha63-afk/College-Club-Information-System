from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubApp', '0002_club_conducted_events_club_upcoming_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='faculty_coordinator',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='club',
            name='student_coordinator',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='club',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='announcement',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='clubApp.club'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='clubApp.club'),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Member', 'Member'), ('Coordinator', 'Coordinator'), ('President', 'President'), ('Secretary', 'Secretary')], default='Member', max_length=30)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='clubApp.club')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_memberships', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='clubApp.event')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_registrations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='membership',
            constraint=models.UniqueConstraint(fields=('student', 'club'), name='unique_student_club_membership'),
        ),
        migrations.AddConstraint(
            model_name='eventregistration',
            constraint=models.UniqueConstraint(fields=('student', 'event'), name='unique_student_event_registration'),
        ),
    ]
