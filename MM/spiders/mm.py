import scrapy
from urllib import request
import os


class Mm(scrapy.Spider):
    name = 'MM'
    start_urls = ['http://www.meizitu.com']

    # 创建文件路径
    def make_dir(self, path):
        path = path.strip()
        path.rstrip("\\")
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
            os.chdir(path)
        else:
            os.chdir(path)

    def parse(self, response):
        self.make_dir('pic')
        urlList = []
        folderList = []
        url = response.xpath(
            ".//div[@id='maincontent']/div[@class='postContent']/div[@id='picture']/p/a/@href").extract()
        folder = response.xpath(
            ".//div[@id='maincontent']/div[@class='postContent']/div[@id='picture']/p/a/@title").extract()
        for u in url:
            urlList.append(u)
        for f in folder:
            folderList.append(f)
        item = dict(zip(folderList, urlList))
        for i in item:
            yield scrapy.Request(url=item[i], callback=self.parse_1)

    def parse_1(self, response):
        urlLists = []
        filenameLists = []
        url = response.xpath(".//div[@class='postContent']/div[@id='picture']/p/img/@src").extract()
        filename = response.xpath(".//div[@class='postContent']/div[@id='picture']/p/img/@alt").extract()

        for u in url:
            urlLists.append(u)
        for f in filename:
            filenameLists.append(f)
        zips = dict(zip(filenameLists, urlLists))
        for key in zips:
            # 模拟浏览器访问（防止反爬虫网站无法爬取）
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            req = request.Request(url=zips[key], headers=headers)
            with request.urlopen(req) as f:
                filename = key + zips[key][-4:]
                data = f.read()
                with open(filename, 'wb') as file:
                    file.write(data)
                    file.close()
