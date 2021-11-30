import scrapy
from scrapy.linkextractors import LinkExtractor


class BingSpider(scrapy.Spider):
    name = "bing"
    search_words = ["john", "doe"]
    forbidden_words = ["bing"]

    def start_requests(self):

        urls = [
            "https://www.bing.com/search?q=" + "+".join(self.search_words)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        xlink = LinkExtractor()
        for link in xlink.extract_links(response):
            does_contain_search_words = [ele for ele in self.search_words if (ele in link.url)]
            does_contain_forbidden_words = [ele for ele in self.forbidden_words if (ele in link.url)]
            if bool(does_contain_search_words) and not does_contain_forbidden_words:
                print(link)
