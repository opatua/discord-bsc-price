import os
from celery import Celery

from config.settings import INSTALLED_APPS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('web')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: INSTALLED_APPS)
