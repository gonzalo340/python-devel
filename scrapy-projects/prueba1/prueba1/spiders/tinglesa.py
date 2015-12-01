import scrapy
import urllib
from scrapy.http import Request, FormRequest
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from prueba1.items import TinglesaItem

class TinglesaSpider(CrawlSpider):
    name = "tinglesa"
    allowed_domains = ["tinglesa.com"]
    start_urls = ['http://www.tinglesa.com.uy/ajax/listado/listadosPaginadoSegunScroll.php?t=%d' %(i) for i in range(82,83)]

    """
    rules = (
        # Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items", follow= True),
	Rule(SgmlLinkExtractor(allow = ('listado.php')), callback = 'parse_items'),
    )
    """

    def start_requests(self):
	for url in self.start_urls:
                url_part = url.split('=')
		print "CATEGORY ID: "  + url_part[1]

		data = { "buscadaDentro": "", "idCategoria": url_part[1], "idListadoEspecial": "", "number": "50", "orden": "", "pagina": "1" }
		#yield Request(url, callback=self.post_data, method="POST", body=urllib.urlencode(data))
		yield FormRequest(url, callback=self.parse_items, formdata=data)


    """
    def parse(self, response):
	data = {"dato": 1, "otro": 2}
        print "PARSE ENTROOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
	yield Request(response.url, callback=self.post_data, method="POST", body=urllib.urlencode(data))
    """

    def parse_items(self, response):
	hxs = HtmlXPathSelector(response)

	r = hxs.xpath("//div").extract()[0]

	body = r
	body = body.replace('\\n', "")
	body = body.replace('\\t', "")
	body = body.replace('\\"', "")

	r2 = HtmlXPathSelector(response.replace(body = body))
	#data = r2.xpath("//div[@class='tabla_subdept']/div[@class='contenedor_items_subdept']/table[@class='item_subdept']")
	data = r2.xpath("//table[@class='item_subdept']")

	for d in data:
		print "SALIDA ITEM FOR"
		#print d.xpath("tr/td[@class='img_prod']").extract()
		print d.xpath("tr/td[@class='img_prod']/a/@href").extract()
		items = []
		#print "DATA: "
		#print data
		#print data.xpath("//div[@class='descripcion_dep']/a/@title").extract()
		#print data.xpath(""i).extract()




    """
    def parse_items(self, response):
	hxs = HtmlXPathSelector(response)

	i= 0
	for obj in hxs.xpath("//div").extract():
		body = obj
		body = body.replace('\\n', "")
		body = body.replace('\\t', "")
		body = body.replace('\\"', "")
		i=i+1

		data = HtmlXPathSelector(response.replace(body = body))
		print "DATA"
		data2 = data.xpath("//div[@class='tabla_subdept']/div[@class='contenedor_items_subdept']")

		for d in data2:
			print "DDDDDDDDDDDDDDDDDDD"
			print d

		items = []
		break
		#print "DATA: "
		#print data
		#print data.xpath("//div[@class='descripcion_dep']/a/@title").extract()
		#print data.xpath(""i).extract()
    """
    """
    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        print "ENTRE"
    """
