# coding=utf-8
class UrlManager(object):

    def __init__(self):
         self.new_urls = set()  # 待爬取url
         self.old_urls = set()  # 已爬取url

    def add_new_url(self, url):    # 向管理器中添加一个新的url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls): # 向管理器中添加新的更多的url
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):  # 判断管理器是否有新的待爬取的url
        return len(self.new_urls) != 0

    def get_new_url(self):  # 从管理器中获取一个新的待爬取的url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

