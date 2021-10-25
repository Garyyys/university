from os import environ as env

from celery import Celery
from celery.schedules import crontab

env.setdefault('DJANGO_SETTINGS_MODULE', 'university.settings')

app = Celery('university')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'heartbeat-daily': {
        'task': 'core.tasks.heart_beat',
        'schedule': crontab(minute='*/1')
    }
}

app.conf.timezone = 'UTC'