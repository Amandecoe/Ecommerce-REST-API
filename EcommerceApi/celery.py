import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EcommerceApi.settings")

app = Celery ("EcommerceApi")
app.config_from_object("django.conf:settings", namespace = "CELERY")
app.autodiscover_tasks()

#scheduled weekly newsletter
app.conf.beat_schedule = {
    "send-weekly-newsletter" : {
        "task" : "ApiApp.tasks.send_weekly_newsletter",
        "schedule" : crontab (hour = 9, minute = 0, day_of_week = "mon") #sends the news letter every monday
    }
}