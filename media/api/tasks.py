import time
from django.http import HttpResponse
from _celery import app
from celery import shared_task
from api.weibo_spider.models import WeiboJoke
from tools.base_func import get_config


@app.task
def test_celery(x, y):
    time.sleep(3)
    print("=====")
    return x * y


def test(request):
    k = test_celery.delay(10, 1)
    print(k)
    return HttpResponse("async tasks")


@shared_task
def weibo_joke_splider():

    user_list = get_config().get("user_id_list", [])
    weibo_info = WeiboJoke()
    for user_id in user_list:
        print(user_id, type(user_id))
        weibo_info.get_weibo_info(user_id=user_id)
        print(u'信息抓取完毕')
        print('*' * 100)
