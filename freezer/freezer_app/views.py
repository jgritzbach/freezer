from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import FoodItem, FoodCategory

# Create your views here.
class Recordset(generic.ListView):
    """
    The view displays all items currently kept in the database as "currently_registered"
    """
    template_name = 'freezer_app/recordset.html'
    context_object_name = 'categories_items_dictionary'


def get_dictionary_of_food_items(show_currently_registered):
    """
    Returns a dictionary where food categories are the keys and currently (non)registered food items associated with that category are the values
    All FoodItem objects known to the freezer registration system are included if their attribute 'currently_registered' is set to the same boolean value as parameter 'show_currently_registered'
    The dictionary serves as a context object for recordset.html template. The template will then show a list of all (non)registered items grouped by their categories.
    """

    food_items = FoodItem.objects.filter(currently_registered=show_currently_registered)    # function returns either registered or non-registered food items
    food_items = food_items.order_by('FoodCategory__name')  # all food items will be ordered by food category name

    categories_items_dictionary = dict()  # each category will become a key in a dictionary and its associated food items will be its values

    for food_item in food_items:                           # let's iterate through all currently (non)registered items
        food_category = food_item.category
        if not food_category in categories_items_dictionary:            # if the category (key) does not exist yet
            categories_items_dictionary[food_category] = []              # let's create it now
        categories_items_dictionary[food_category].append(food_item)       # and add iterated food item to it

    return categories_items_dictionary