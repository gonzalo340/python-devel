from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from prueba1.items import CatalogoSegagamesItem


class SegagamesSpider(BaseSpider):
    name = "sega"
    allowed_domains = ["segagames.cu.cc"]
    start_urls = ["http://www.segagames.cu.cc/categories"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
	#data = hxs.select("//div[@class='container']")

	data = hxs.select("//a[re:test(@href, '/categories/view/.*$')]")

	for d in data:
	    name = d.select("div[@class='category']/div[@class='container']/div[@class='name']/text()").extract()
	    image = d.select("div[@class='category']/div[@class='container']/img/@src").extract()
	    link = d.re(r'<a href="(.*\d)">')
	    print name,image,link
"""
        for d in data:
            _name = d.select("div/text()").extract()
	    _image = d.select("img/@src").extract()
            _link ='Sin definir'
            print _name, _image, _link
"""
