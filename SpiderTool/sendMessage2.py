import mysql.connector
#! /usr/bin/env python2
# encoding:utf-8
# python 2.7 测试通过
# python 3 更换适当的开发库就能使用，在此我们不额外提供

import http.client
import json
import hashlib
import random
import time


# 定义发送短信的类
class SmsSender:
    sdkappid = 0
    appkey = ""
    # API发送短信的文档

    url = "https://yun.tim.qq.com/v5/tlssmssvr/sendsms"

    # 构造函数，把appid和appkey传入
    def __init__(self, sdkappid, appkey):
        self.sdkappid = sdkappid
        self.appkey = appkey

    # 发短信的函数，传入国家码，手机号和内容
    def sendMsg(self, nationCode, phoneNumber, content):
        # 接口定义的appkey+phoneNumber的md5()变量

        rnd = random.randint(1000000000, 9999999999)
        t = int(time.time())
        s = ("appkey=" + self.appkey + "&random=" + str(rnd) + "&time=" + str(t) + "&mobile=" + phoneNumber).encode("utf-8")
        sig = hashlib.sha256(s).hexdigest()
        print(content)
        pkg = {
            "ext": "",
            "extend": "",
            "msg": content,
            "sig": sig,
            "tel": {
                "mobile": phoneNumber,
                "nationcode": nationCode
            },
            "time": t,
            "type": 0
        }

        con = None
        try:
            con = http.client.HTTPSConnection('yun.tim.qq.com', timeout=10)
            body = json.dumps(pkg)
            wholeUrl = '%s?sdkappid=%d&random=%d' % (self.url, self.sdkappid, rnd)
            con.request('POST', wholeUrl, body)
            response = con.getresponse()
            print(response.status, response.reason)
            data = response.read()
            print(data)
        except Exception as e:
            print(e)
        finally:
            if (con):
                con.close()


if __name__ == "__main__":
    conn = mysql.connector.connect(user='root', password='135213521352', database='mysql')
    cursor = conn.cursor()
    # 开放者实际发送短信时请使用申请的 sdkappid 和 appkey
    # 定义3个变量
    sql = """
        select * from douban_rent where `douban_rent`.`status`=0;
    """
    sql_update = """
        update douban_rent SET `douban_rent`.`status` = 1 where `douban_rent`.`status` = 0 
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.execute(sql_update)
    conn.commit()
    for result in results:
        title = str(result[0])
        url = str(result[1])
        # 创建对象
        sender = SmsSender(1400092370, "ae30aa4bc2785bb6491c1a2ffb0bf9e8")
        # 要发送的手机号码
        phones = [
                  "17616271667",
                  
                  ]
        for phone in phones:
            sender.sendMsg("86", phone, "电影名称《找房记》,评分"+"：负分，主演："  + url)
