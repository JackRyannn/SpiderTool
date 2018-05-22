import mysql.connector
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpidertoolPipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='135213521352', database='mysql')
        self.cursor = self.conn.cursor()



    def process_item(self, item, spider):

        title = item.get('title')[0]
        score = item.get('score')[0]
        star = item.get('star')[0]
        release = item.get('release')[0]
        duration = item.get('duration')[0]
        director = item.get('director')[0]
        actors = item.get('actors')[0]
        region = item.get('region')[0]
        category = item.get('category')[0]
        enough = item.get('enough')[0]
        showed = item.get('showed')[0]
        votecount = item.get('votecount')[0]
        subject = item.get('subject')[0]
        pic = item.get('pic')[0]
        
        
        insert_sql = """
            insert ignore into douban_movie(`data-title`,`data-score`,`data-star`,`data-release`,`data-duration`,`data-director`,`data-actors`,`data-region`,`data-category`,`data-enough`,`data-showed`,`data-votecount`,`data-subject`,pic)
            VALUES (%s, %s, %s, %s ,%s, %s, %s, %s, %s ,%s, %s, %s, %s, %s);
        """
        self.cursor.execute(insert_sql, (title,score,star,release,duration,director,actors,region,category,enough,showed,votecount,subject,pic))
        self.conn.commit()

        return item

    def close_spider(self, spider):
        select_send_sql = """
            select * from douban_movie,douban_movie_send WHERE douban_movie.`data-subject` not in (select douban_movie_send.`data-subject` from douban_movie_send) ORDER BY `data-score` DESC LIMIT 1;
                """
        self.cursor.execute(select_send_sql)
        result = self.cursor.fetchall()

        send_subject = result[0][12]

        insert_send_sql = """
                    insert into douban_movie_send(`data-subject`) 
                    VALUES (%s); 
                """

        self.cursor.execute(insert_send_sql, (send_subject,))
        self.conn.commit()

        self.cursor.close()
        self.conn.close()
