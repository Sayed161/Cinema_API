import os
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema.settings')

app = Celery('cinema')


app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_ranking_task':{
        'task':'movies.tasks.update_ranking',
        'schedule': timedelta(minutes=5)
    }
}