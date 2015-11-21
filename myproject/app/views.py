from django.shortcuts import render
from app.models import scraped_item
from app.serializers import scraped_item_serilizer
from rest_framework import viewsets
# Create your views here.
class scraped_item_viewset(viewsets.ModelViewSet):
	queryset = scraped_item.objects.all()
	serializer_class=scraped_item_serilizer