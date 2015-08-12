#!/usr/bin/env python
import csv
import os
import sys


sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import Cereal, Manufacturer, Nutritionam_Facts

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cereal.csv')

csv_file = open(csv_file_path, 'r')

# print csv_file

reader = csv.DictReader(csv_file)

for row in reader:
	print row
	# print row ['Cereal Name'].replace('_', ' ')
	# print row ['Manufacturer']

	manu_obj, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])
	# manu_obj.name = row['Manufacturer']
	# manu_obj.save()
	
	cereal_obj, created = Cereal.objects.get_or_create(name=row['Cereal Name'].replace('_'), ' ')
	cereal_obj.name = row['Cereal Name']
	cereal_obj.c_type = row['Type']
	cereal_obj.display_shelf = row['Display Shelf']
	cereal_obj.serving_size_weight = row['Serving Size Weight']
	cereal_obj.cups_per_serving = row['Cups per Serving']
	cereal_obj.manufacturer = manu_obj
	cereal_obj.save()

	nutr_obj, created = Nutritionam_Facts.objects.get_or_create(cereal=cereal_obj)
	nutr_obj.calories = row['Calories']
	nutr_obj.protein = row['Protein (g)']
	nutr_obj.fat = row['Fat']
	nutr_obj.sodium = row['Sodium']
	nutr_obj.dietary_fiber = row['Dietary Fiber']
	nutr_obj.carbs = row['Carbs']
	nutr_obj.sugar = row['Sugars']
	nutr_obj.potassium = row['Potassium']
	nutr_obj.vitamins_and_minerals = row['Vitamins and Minerals']
	nutr_obj.save()

	# print row ['Type']
	# print row ['Calories']
	# print row ['Protein (g)']
	# print row ['Fat']
	# print row ['Sodium']
	# print row ['Dietary Fiber']
	# print row ['Carbs']
	# print row ['Sugars']
	# print row ['Display Shelf']
	# print row ['Potassium']
	# print row ['Vitamins and Minerals']
	# print row ['Serving Size Weight']
	# print row ['Cups Per Serving']