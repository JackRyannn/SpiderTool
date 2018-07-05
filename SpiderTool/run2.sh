cd /var/www/douban/SpiderTool/ && /usr/local/bin/scrapy crawl rent
sleep 10
/usr/local/bin/python3 /var/www/douban/SpiderTool/SpiderTool/sendMessage2.py
