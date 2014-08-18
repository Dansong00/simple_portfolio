from django.db import models

# Create your models here.
class Item(models.Model):
		publish_date = models.DateField(max_length=200)
		name = models.CharField(max_length=200)
		details = models.CharField(max_length=1000)
		url = models.URLField(null=True)
		thumbnail = models.CharField(max_length=200,null=True)
		