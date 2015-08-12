from django.db import models

# Create your models here.

class Manufacturer(models.Model):
	name = models.CharField(max_length = 30, unique = True)

	def __unicode__(self):
		return self.name

class Cereal(models.Model):
	name = models.CharField(max_length = 30, null = True)
	c_type = models.CharField(max_length  = 2, null = True)
	display_shelf = models.IntegerField(null = True)
	serving_size_weight = models.FloatField(null = True)
	cups_per_serving = models.FloatField(null = True)
	manufacturer = models.ForeignKey('main.Manufacturer', null = True)
	
	def __unicode__(self):
		return self.name

class Nutritionam_Facts(models.Model):
	calories = models.IntegerField(null = True)
	protein = models.IntegerField(null = True)
	fat = models.IntegerField(null = True)
	sodium = models.FloatField( null = True)
	dietary_fiber = models.FloatField(null = True)
	carbs = models.FloatField(null = True)
	sugar = models.FloatField(null = True)
	potassium = models.IntegerField(null = True)
	vitamins_and_minerals = models.IntegerField(null = True)
	cereal = models.OneToOneField('main.Cereal', null = True)

	def __unicode__(self):
		return self.cereal.name

	def nutrition_list(self):
		value_list = []
		value_list.append("protein: %s" % self.protein)
		value_list.append("calories: %s" % self.calories)
		value_list.append("fat: %s" % self.fat)
		value_list.append("sodium: %s" % self.sodium)
		value_list.append("dietary fiber: %s" % self.dietary_fiber)
		value_list.append("carbs: %s" % self.carbs)
		value_list.append("sugar: %s" % self.sugar)
		value_list.append("potassium: %s" % self.potassium)
		value_list.append("vitamins & minerals: %s " % self.vitamins_and_minerals)

		return value_list
