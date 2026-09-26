# Upgraded version of your original clubApp

This project is based on the uploaded `clubApp(1).zip`. The original club pages,
login/signup flow, college image, clubs, events and announcements were retained,
then upgraded with:

- Real `Event` records linked to clubs
- Student `Membership` records
- Join Club button
- Event registration
- My Clubs dashboard
- My Events dashboard
- Club coordinators/contact information
- Announcement-to-club linking
- Improved Bootstrap UI
- Expanded Django admin

## Run

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

Create an admin account if needed:

```bash
python manage.py createsuperuser
```

Then use `/admin/` to add clubs, events and announcements.
