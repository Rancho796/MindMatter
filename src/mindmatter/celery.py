from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

#Set default Django settings module for celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mindmatter.settings')

#Initilaize Celery app
app = Celery('mindmatter')

#Load settings from django settings file
app.config_from_object('django.conf:settings',namespace='CELERY')

#Auto-discover tasks from registered Django apps
app.autodiscover_tasks()