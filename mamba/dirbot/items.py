from scrapy.item import Item, Field


class Website(Item):
    name = Field()
    url=Field()
    description=Field()
    paginator=Field()


class Mamba(Item):
    user = Field()
    url = Field()
    number = Field()


class CraigslistSampleItem(Item):
    title = Field()
    link = Field()
    number = Field()


class Google(Item):
    site = Field()
    number=Field()

class DmozItem(Item):
    title=Field()
    link=Field()
    desk=Field()

class Article(Item):
    title=Field()

class MagazineCover(Item):
    title=Field()
    pubDate=Field()
    file_urls=Field()