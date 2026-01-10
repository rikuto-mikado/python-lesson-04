from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Saladas"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
)


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.CharField(decimial_price=2)
    meal_type = models.CharField(choice=MEAL_TYPE)
    author = models.ForeignKey(User)
