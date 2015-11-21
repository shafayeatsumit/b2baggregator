from app.models import scraped_item
from rest_framework import serializers

class scraped_item_serilizer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	class Meta:
		model = scraped_item
		fields = ('id','title', 'location', 'posting_time', 'category','price','link')
