from django.db import models

# Create your models here.
class scraped_item(models.Model):
	title=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	posting_time=models.CharField(max_length=100)
	category=models.CharField(max_length=100)
	price=models.CharField(max_length=100)
	link=models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.title
