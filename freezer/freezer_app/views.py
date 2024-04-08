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