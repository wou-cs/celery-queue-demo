import time

from celery import Celery

celery = Celery(
    'tasks',
    backend='redis://localhost/',
    broker='redis://localhost/'
    )

@celery.task
def add(x, y):
    time.sleep(5)
    return x + y
