import time
from django.http import HttpResponse
from media._celery import app
from celery import shared_task


@app.task
def test_celery(x, y):
    time.sleep(3)
    return x * y


def test(request):
    k = test_celery.delay(10, 1)
    print(k)
    return HttpResponse("async tasks")


@shared_task
def something():
    print("haha")
    return "crontab tasks"
