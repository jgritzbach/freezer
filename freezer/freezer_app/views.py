from typing import Any
from django.db.models.query import QuerySet
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

    def get_queryset(self):
        return get_dictionary_of_food_items(True)
    
    def post(self, request):
        """
        The view processes POST requests from the form in recordset.html template
        """

        food_item = FoodItem.objects.get(id=request.POST.get('id'))  # Each item listed in the recordset has its own <form> element. Depending on which form in the template was called, we know the ID of the item. So we'll pull it from the database
        
        # Which button was clicked in the form?

        # Amount manipulation
        if 'amount' in request.POST:
            amount = int(request.POST.get('amount'))     # the amount to be edited based on form submit

            if food_item.amount + amount >=0:  # going below zero amount is not allowed
                food_item.amount += amount
                food_item.save()

        # Removing completely from the recordset
        elif 'remove-item' in request.POST:
            food_item.amount = 0
            food_item.currently_registered = False
            food_item.save()

        return redirect('recordset')    # after processing the POST request, we'll redirect the user back to the recordset view       


def get_dictionary_of_food_items(show_currently_registered):
    """
    Returns a dictionary where food categories are the keys and currently (non)registered food items associated with that category are the values
    All FoodItem objects known to the freezer registration system are included if their attribute 'currently_registered' is set to the same boolean value as parameter 'show_currently_registered'
    The dictionary serves as a context object for recordset.html template. The template will then show a list of all (non)registered items grouped by their categories.
    """

    food_items = FoodItem.objects.filter(currently_registered=show_currently_registered)    # function returns either registered or non-registered food items
    food_items = food_items.order_by('category__name')  # all food items will be ordered by food category name

    categories_items_dictionary = dict()  # each category will become a key in a dictionary and its associated food items will be its values

    for food_item in food_items:                           # let's iterate through all currently (non)registered items
        food_category = food_item.category
        if not food_category in categories_items_dictionary:            # if the category (key) does not exist yet
            categories_items_dictionary[food_category] = []              # let's create it now
        categories_items_dictionary[food_category].append(food_item)       # and add iterated food item to it

    return categories_items_dictionary