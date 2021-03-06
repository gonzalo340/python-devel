from scrapy.contrib.spiders import CrawlSpider, Rule, BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from prueba1.items import TinglesaItem

"""class TinglesaSpider(CrawlSpider):"""
class TinglesaSpider(BaseSpider):
    name = "tinglesa"
    allowed_domains = ["tinglesa.com.uy"]
    start_urls = ["http://www.tinglesa.com.uy"]
    """
    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="link"]',)), callback="parse_items", follow= True),
    )
    """
    #def parse_items(self, response):
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        data = hxs.xpath('//table[@class="carousel_cont"]')
        items = []
        for d in data:
            item = TinglesaItem()
            item["nombre"] = d.xpath("td@[class='titulo']/a/text()").extract()
            item["precio"] = d.xpath("td@[class='precio']/text()").extract()
            # item[""]
            items.append(item)
        return(items)
