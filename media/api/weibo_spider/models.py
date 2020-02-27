import pymongo
import time
import requests
import datetime
import copy
import csv
import json
import os
import random
import re
import sys
import traceback

from collections import OrderedDict
from tqdm import tqdm
from lxml import etree
from datetime import date, datetime, timedelta
from requests.adapters import HTTPAdapter
from tools.base_mongo import MongoService
from tools.base_func import get_config


class WeiboJoke(object):
    Joke_Fields = ["id", "content", "video_url", "publish_time", "up_num", "retweet_num", "comment_num"]

    def __init__(self):
        mogo_info = MongoService()
        self.db = mogo_info.connect_weibo()
        self.joke = self.db.joke
        self.got_num = 0

    def joke_insert_db(self, data):
        result = self.joke.insert(data)
        import ipdb
        ipdb.set_trace()
        print(result)

    @property
    def since_date(self):
        since_date = (datetime.now() + timedelta(days=-1)).strftime('%Y-%m-%d')

        return since_date

    @property
    def cookie(self):
        cookie = get_config().get("cookie", "")
        if not cookie:
            raise Exception("获取cookie失败")

        return {"Cookie": cookie}

    def handle_html(self, url):
        """处理html"""
        try:
            html = requests.get(url, cookies=self.cookie).content
            selector = etree.HTML(html)
            return selector
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()

    def handle_garbled(self, info):
        """处理乱码"""
        try:
            info = (info.xpath('string(.)').replace(u'\u200b', '').encode(
                sys.stdout.encoding, 'ignore').decode(sys.stdout.encoding))
            return info
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()

    def get_nickname(self, user_id):
        """获取用户昵称"""
        try:
            url = 'https://weibo.cn/%s/info' % (user_id)
            selector = self.handle_html(url)
            nickname = selector.xpath('//title/text()')[0]
            nickname = nickname[:-3]
            if nickname == u'登录 - 新' or nickname == u'新浪':
                raise Exception(u'cookie错误或已过期,请按照README中方法重新获取')
            return nickname
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()

    def get_user_info(self, selector, user_id):
        """获取用户昵称、微博数、关注数、粉丝数"""
        try:
            nick_name = self.get_nickname(user_id=user_id)  # 获取用户昵称
            user_info = selector.xpath("//div[@class='tip2']/*/text()")
            weibo_num = int(user_info[0][3:-1])
            following = int(user_info[1][3:-1])
            followers = int(user_info[2][3:-1])
            print(u'用户昵称: %s' % nick_name)
            print(u'用户id: %s' % user_id)
            print(u'微博数: %d' % weibo_num)
            print(u'关注数: %d' % following)
            print(u'粉丝数: %d' % followers)
        except Exception as e:
            print('Error: ', "获取用户信息失败")
            traceback.print_exc()

    def is_pinned_weibo(self, info):
        """判断微博是否为置顶微博"""
        kt = info.xpath(".//span[@class='kt']/text()")
        if kt and kt[0] == u'置顶':
            return True
        else:
            return False

    def get_page_num(self, selector):
        """获取微博总页数"""
        try:
            if selector.xpath("//input[@name='mp']") == []:
                page_num = 1
            else:
                page_num = (int)(
                    selector.xpath("//input[@name='mp']")[0].attrib['value'])
            return page_num
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()

    def get_weibo_footer(self, info):
        """获取微博点赞数、转发数、评论数"""
        try:
            footer = {}
            pattern = r'\d+'
            str_footer = info.xpath('div')[-1]
            str_footer = self.handle_garbled(str_footer)
            str_footer = str_footer[str_footer.rfind(u'赞'):]
            weibo_footer = re.findall(pattern, str_footer, re.M)

            up_num = int(weibo_footer[0])
            footer['up_num'] = up_num

            retweet_num = int(weibo_footer[1])
            footer['retweet_num'] = retweet_num

            comment_num = int(weibo_footer[2])
            footer['comment_num'] = comment_num
            return footer
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()

    def get_publish_time(self, info):
        """获取微博发布时间"""
        try:
            str_time = info.xpath("div/span[@class='ct']")
            str_time = self.handle_garbled(str_time[0])
            publish_time = str_time.split(u'来自')[0]
            if u'刚刚' in publish_time:
                publish_time = datetime.now().strftime('%Y-%m-%d %H:%M')
            elif u'分钟' in publish_time:
                minute = publish_time[:publish_time.find(u'分钟')]
                minute = timedelta(minutes=int(minute))
                publish_time = (datetime.now() -
                                minute).strftime('%Y-%m-%d %H:%M')
            elif u'今天' in publish_time:
                today = datetime.now().strftime('%Y-%m-%d')
                time = publish_time[3:]
                publish_time = today + ' ' + time
                if len(publish_time) > 16:
                    publish_time = publish_time[:16]
            elif u'月' in publish_time:
                year = datetime.now().strftime('%Y')
                month = publish_time[0:2]
                day = publish_time[3:5]
                time = publish_time[7:12]
                publish_time = year + '-' + month + '-' + day + ' ' + time
            else:
                publish_time = publish_time[:16]
            return publish_time
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()

    def get_weibo_content(self, info):
        """获取微博内容"""
        try:
            weibo_id = info.xpath('@id')[0][2:]

            weibo_content = self.handle_garbled(info)
            weibo_content = weibo_content[:weibo_content.rfind(u'赞')]
            a_text = info.xpath('div//a/text()')
            if u'全文' in a_text:
                weibo_link = 'https://weibo.cn/comment/' + weibo_id

                # 长原创微博
                selector = self.handle_html(weibo_link)
                info = selector.xpath("//div[@class='c']")[1]
                wb_content = self.handle_garbled(info)
                wb_time = info.xpath("//span[@class='ct']/text()")[0]
                weibo_content = wb_content[wb_content.find(':') + 1:wb_content.rfind(wb_time)]

                if wb_content:
                    weibo_content = wb_content
            return weibo_content
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()

    def get_video_url(self, info, is_original):
        """获取微博视频url"""
        try:
            video_url = u"无"
            if is_original:
                div_first = info.xpath('div')[0]
                a_list = div_first.xpath('.//a')
                video_link = u'无'
                for a in a_list:
                    if 'm.weibo.cn/s/video/show?object_id=' in a.xpath(
                            '@href')[0]:
                        video_link = a.xpath('@href')[0]
                        break
                if video_link != u'无':
                    video_link = video_link.replace(
                        'm.weibo.cn/s/video/show', 'm.weibo.cn/s/video/object')
                    wb_info = requests.get(video_link, cookies=self.cookie).json()
                    video_url = wb_info['data']['object']['stream'].get(
                        'hd_url')
                    if not video_url:
                        video_url = wb_info['data']['object']['stream']['url']
                        if not video_url:  # 说明该视频为直播
                            video_url = u'无'
            else:
                video_url = u'无'
            return False if video_url == u'无' else True
        except Exception:
            return False

    def extract_picture_urls(self, info, weibo_id):
        """提取微博原始图片url"""
        try:
            a_list = info.xpath('div/a/@href')
            first_pic = 'https://weibo.cn/mblog/pic/' + weibo_id + '?rl=0'
            all_pic = 'https://weibo.cn/mblog/picAll/' + weibo_id + '?rl=1'
            if first_pic in a_list:
                if all_pic in a_list:
                    selector = self.handle_html(all_pic)
                    preview_picture_list = selector.xpath('//img/@src')
                    picture_list = [
                        p.replace('/thumb180/', '/large/')
                        for p in preview_picture_list
                    ]
                    picture_urls = ','.join(picture_list)
                else:
                    if info.xpath('.//img/@src'):
                        preview_picture = info.xpath('.//img/@src')[-1]
                        picture_urls = preview_picture.replace(
                            '/wap180/', '/large/')
                    else:
                        sys.exit(
                            u"爬虫微博可能被设置成了'不显示图片'，请前往"
                            u"'https://weibo.cn/account/customize/pic'，修改为'显示'"
                        )
            else:
                picture_urls = u'无'
            return picture_urls
        except Exception as e:
            return u'无'

    def get_picture_urls(self, info):
        """获取微博原始图片url"""
        try:
            weibo_id = info.xpath('@id')[0][2:]
            picture_urls = {}
            original_pictures = self.extract_picture_urls(info, weibo_id)
            picture_urls['original_pictures'] = original_pictures
            return picture_urls
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()

    def get_one_weibo(self, info):
        """获取一条微博的全部信息"""
        try:
            weibo = OrderedDict()
            is_original = info.xpath("div/span[@class='cmt']")
            if len(is_original) > 3:
                return False

            if self.get_video_url(info, is_original):
                return False

            weibo['id'] = info.xpath('@id')[0][2:]
            weibo['content'] = self.get_weibo_content(info)  # 微博内容
            picture_urls = self.get_picture_urls(info)
            weibo['original_pictures'] = picture_urls['original_pictures']  # 原创图片url

            weibo['publish_time'] = self.get_publish_time(info)  # 微博发布时间
            footer = self.get_weibo_footer(info)
            weibo['up_num'] = footer['up_num']  # 微博点赞数
            weibo['retweet_num'] = footer['retweet_num']  # 转发数
            weibo['comment_num'] = footer['comment_num']  # 评论数

            return weibo
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()

    def get_one_page(self, page, user_id):
        """获取第page页的全部微博"""
        try:
            url = 'https://weibo.cn/u/%s?page=%d' % (user_id, page)
            selector = self.handle_html(url)
            info = selector.xpath("//div[@class='c']")
            is_exist = info[0].xpath("div/span[@class='ctt']")
            weibo_id_list = []
            if is_exist:
                for i in range(0, len(info) - 2):
                    weibo = self.get_one_weibo(info[i])
                    if weibo:
                        if weibo['id'] in weibo_id_list:
                            continue
                        publish_time = datetime.strptime(weibo['publish_time'][:10], "%Y-%m-%d")
                        since_date = datetime.strptime(self.since_date, "%Y-%m-%d")
                        if publish_time < since_date:
                            if self.is_pinned_weibo(info[i]):
                                continue
                            else:
                                return True

                        self.joke_insert_db(weibo)
                        weibo_id_list.append(weibo['id'])
                        self.got_num += 1
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()

    def get_weibo_info(self, user_id):
        """获取微博信息"""
        try:
            url = 'https://weibo.cn/u/%s' % (user_id)
            selector = self.handle_html(url)
            self.get_user_info(selector, user_id)  # 获取用户昵称、微博数、关注数、粉丝数
            page_num = self.get_page_num(selector)  # 获取微博总页数
            page1 = 0
            random_pages = random.randint(1, 5)
            for page in tqdm(range(1, page_num + 1), desc='Progress'):
                print(page)
                is_end = self.get_one_page(page, user_id=user_id)  # 获取第page页的全部微博
                if is_end:
                    break

                # 通过加入随机等待避免被限制。爬虫速度过快容易被系统限制(一段时间后限
                # 制会自动解除)，加入随机等待模拟人的操作，可降低被系统限制的风险。默
                # 认是每爬取1到5页随机等待6到10秒，如果仍然被限，可适当增加sleep时间
                if page - page1 == random_pages and page < page_num:
                    time.sleep(random.randint(6, 10))
                    page1 = page
                    random_pages = random.randint(1, 5)

            print(u'共爬取' + str(self.got_num) + u'条原创微博')
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()
