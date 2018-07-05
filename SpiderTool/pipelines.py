import mysql.connector
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpidertoolPipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='123456', database='mysql')
        self.cursor = self.conn.cursor()



    def process_item(self, item, spider):

        title = item.get('title')[0]
        url = item.get('url')[0]

        insert_sql = """
            insert ignore into douban_rent(`title`,`url`)
            VALUES (%s, %s);
        """
        self.cursor.execute(insert_sql, (title,url))
        print("重要：",title,url)
        self.conn.commit()

        return item

    def close_spider(self, spider):
        select_send_sql = """
                select * from douban_rent WHERE douban_rent.`url` not in (select douban_rent_send.`url` from douban_rent_send);
                """
        self.cursor.execute(select_send_sql)
        result = self.cursor.fetchall()

        insert_send_sql = """
                    insert into douban_rent_send(`url`)
                    VALUES (%s);
                """
        for i in range(len(result)):
            send_subject = result[i][1]
            self.cursor.execute(insert_send_sql, (send_subject,))
        self.conn.commit()

        self.cursor.close()
        self.conn.close()
