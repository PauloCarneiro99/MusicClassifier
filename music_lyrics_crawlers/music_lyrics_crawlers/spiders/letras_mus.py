import scrapy
import logging

from scrapy.spiders import Spider
from ..items import LyricsItem


class LetrasMus(Spider):
    name = "letras_mus"

    logger = logging.getLogger(__name__)

    start_urls = ["https://www.letras.mus.br/estilos/"]

    base_url = "https://www.letras.mus.br"
    style_page = "https://www.letras.mus.br/mais-acessadas/{0}/"

    def parse(self, response):
        """Parse the https://www.letras.mus.br/estilos/ page, iterating for each style
        
        Arguments:
            response {scrapy.http.response.html.HtmlResponse} -- [html response]
        """
        styles_xpath = response.xpath("//ul[@class='cnt-list cnt-list--col2']/li//a")

        for style_it in styles_xpath:
            style = style_it.xpath("./text()").get().strip().lower()

            self.logger.info(f"Crawling style = {style}")
            yield scrapy.Request(
                url=self.style_page.format(style),
                callback=self.parse_style_page,
                meta={"style": style},
            )

    def parse_style_page(self, response):
        """For each style, iterate for the first thousand most famous musics
        
        Arguments:
            response {scrapy.http.response.html.HtmlResponse} -- [html response for the most popular musics for this style]
        """
        music_url = response.xpath(
            "//ol[@class='top-list_mus cnt-list--col1-3']/li/a/@href"
        ).extract()

        for url in music_url:
            url = self.base_url + url
            yield scrapy.Request(url=url, callback=self.parse_lyrics, meta=response.meta)

    def parse_lyrics(self, response):
        """Get the content of this music page
        
        Arguments:
            response {scrapy.http.response.html.HtmlResponse} -- [html response for the music page]
        """
        item = LyricsItem()

        item["style"] = response.meta["style"]
        item["title"] = response.xpath("//div[@class='cnt-head_title']/h1/text()").get().strip()
        item["author"] = response.xpath("//div[@class='cnt-head_title']/h2/a/text()").get().strip()
        item["lyrics"] = response.xpath("//div[@class='cnt-letra p402_premium']/p/text()").extract()

        item["data"] = {}
        item["data"]["url"] = response.url

        yield item
