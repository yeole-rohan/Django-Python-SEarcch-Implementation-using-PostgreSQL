from django.db import models


# Create your models here.
class RestaurantDetails(models.Model):
	restaurant_id = models.CharField(max_length=20,unique=True)
	restaurant_name = models.CharField(max_length=200)
	cuisines = models.CharField(max_length=200)
	average_cost_for_two = models.CharField(max_length=50)
	currency = models.CharField(max_length=20)
	has_table = models.CharField(max_length=50)
	has_online = models.CharField(max_length=50)
	rating = models.CharField(max_length=10)
	rating_color = models.CharField(max_length=20)
	rating_text = models.CharField(max_length=20)
	votes = models.CharField(max_length=20)
	
	def init(self):
		return self.restaurant_id


class RestaurantAddress(models.Model):
	restaurant = models.CharField(max_length=200)
	country_code = models.CharField(max_length=20)
	city = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	locality = models.CharField(max_length=200)
	locality_verbose = models.CharField(max_length=200)
	longitude = models.CharField(max_length=200)
	latitude = models.CharField(max_length=200)


