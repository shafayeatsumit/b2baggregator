import scrapy
from scrapy_djangoitem import DjangoItem
from app.models import scraped_item

class DmozItem(DjangoItem):
	django_model = scraped_item