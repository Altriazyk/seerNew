import requests
import json
import time
import random

from core.client import webSocketClient
from function.Algorithm import md5


def get_current_timestamp() -> int:
    return int(round(time.time() * 1000))


def jquery_mock_callback() -> str:
    return "jQuery" + ('1.7.2' + str(random.random())).replace(".", "") + "_" + str(get_current_timestamp() - 1000)


def get_session(account, password):
    callback = jquery_mock_callback()
    timestamp = get_current_timestamp()
    # 目标网页的URL
    url = 'https://account-co.61.com/index.php?r=userIdentity/authenticate&callback=' + callback + '&account=' + account + '&rememberAcc=false&passwd=' + password + '&rememberPwd=true&vericode=&game=02&tad=none&_=' + str(
        timestamp) + '/authenticate/login&gid=206&tad=none'
    # 发起GET请求
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        data = response.text
        # 移除前缀和尾部的分号
        cleaned_response = response.text.split('(')[1].split(')')[0]
        # 解析JSON字符串
        data = json.loads(cleaned_response)
        # 访问session值
        session_value = data['data']['session']
        return session_value
    else:
        # 如果请求不成功，打印错误信息和状态码
        print(f"Request failed with status code: {response.status_code}")


def loginGame(account, password):
    webSocketClient.uid = hex(int(account))[2:]
    password = md5(password)
    session = get_session(account, password)
    testLogin = '000000a931000003e9' + hex(int(account))[
                                       2:] + '00000000' + session + '74616f6d656500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003ee00000000504300000000000000000000000000000000000000000001000000010000000168355f7765625f74616f6d656500000000000000000000000000000000000000'
    webSocketClient.send_message(testLogin)
