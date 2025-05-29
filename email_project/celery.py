import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_project.settings')

app = Celery('email_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Celery Beat Schedule
app.conf.beat_schedule = {
    'send-email-every-minute': {
        'task': 'mailapp.tasks.send_scheduled_email',
        'schedule': 60.0,  # every 60 seconds
    },
}
