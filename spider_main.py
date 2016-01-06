# coding=utf-8
from baike_spider import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()    #url管理器
        self.downloader = html_downloader.HtmlDownloader()  #下载器
        self.parser = html_parser.HtmlParser()  #解析器
        self.outputer = html_outputer.HtmlOutputer()    #输出器

    def craw(self, root_url):
        count = 1 #判断当前爬取的是第几个url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():      #循环,爬取所有相关页面,判断异常情况
            try:
                new_url = self.urls.get_new_url()   #取得url
                print 'craw %d : %s' % (count, new_url) #打印当前是第几个url
                html_cont = self.downloader.download(new_url)   #下载页面数据
                new_urls, new_data = self.parser.parse(new_url,html_cont)    #进行页面解析得到新的url以及数据

                self.urls.add_new_urls(new_urls) #添加新的url
                self.outputer.collect_data(new_data) #收集数据

                if count == 10:  # 此处10可以改为100甚至更多,代表循环次数
                    break

                count = count + 1
            except:
                print 'craw failed'

        self.outputer.output_html()   #利用outputer输出收集好的数据

if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()   # 创建
    obj_spider.craw(root_url)   # craw方法启动爬虫