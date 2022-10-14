from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .services import *
import datetime


@periodic_task(run_every=(crontab(minute = "*" , hour='00-23')))
def populate_db_objects():
    print("Running every 60 seconds. Last successful run at -", datetime.datetime.now()-datetime.timedelta(minutes=1))
    populate_db()
