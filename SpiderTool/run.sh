cd /var/www/douban/SpiderTool/ && /usr/local/bin/scrapy crawl mt
sleep 10
/usr/local/bin/python3 /var/www/douban/SpiderTool/SpiderTool/sendMessage.py
touch /var/www/douban/SpiderTool/SpiderTool/001.txt
