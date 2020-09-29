#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, as_completed, ALL_COMPLETED
import random
import miaomiao
import atexit

FLAG = False


def test333(n):
    time.sleep(n)
    print(f'{current_thread().name}>>>>{n} begin')
    if n == 0:
        exit(0)
    time.sleep(3)
    print(f'{current_thread().name}>>>>{n} done')


import asyncio
import time
import requests
from itertools import chain


async def say_after(delay, what):
    res = await requests.get('https://miaomiao.scmttec.com/seckill/seckill/now2.do')
    # await asyncio.sleep(delay)
    print(res.json())


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    # print('----------')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


def init_ip_proxy_pool(pages: int = 2) -> list:
    """
    填充临时IP代理池。（考虑到秒杀场景瞬时性,提前初始化可用的IP代理 避免秒杀中临时调用API）

    IP代理来源
        1.使用收费的代理商提供
        2.自建IP代理池
            - 爬取免费IP代理
            - 验证IP可用
            - 持久化
            - 定时更新可用IP

    这里直接使用第三方提供的API(避免自建轮子、搭建环境。测试)：https://github.com/jiangxianli/ProxyIpLib
    :return: ip代理池列表
    """
    ip_proxy_res = [miaomiao.MiaoMiao.get_proxy_ip(p)['data']['data'] for p in range(1, pages + 1)]
    return [f'{data["ip"]}:{data["port"]}' for data in list(chain(*ip_proxy_res))]


def test3333(paxm, **kwargs):
    print(paxm, kwargs)
    # time.sleep(random.randint(1, 3))
    # res = requests.get('https://baidu.com', proxies=pax, verify=False)
    #
    # print(res.status_code)
    # pr
    #
    # int('====================')


def test1(n):
    try:
        r = 1/n
    except Exception as e:
        print(e)
    else:
        return r

if __name__ == '__main__':
    # s1 = test1(0)
    l1 = [(v1 := test1(x)) for x in [0,0]]
    print(l1,len(l1))