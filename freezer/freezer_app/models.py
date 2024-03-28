from django.db import models

# Create your models here.
class FoodCategory (models.Model):
    """
    This model represents the food category, e.g. 'main course', 'soup', 'semi-finished product' etc.
    """
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Food category'
        verbose_name_plural = 'Food categories'


class FoodItem(models.Model):
    """
    This model represents a specific item that can be registered in the freezer, e.g. 'beef stew'.
    It is expected to fall under some FoodCategory, e.g. 'main course'.
    The item holds an awareness of whether it is currently registered in the freezer at all or not.
    It is also described by an amount (a non-negative integer).
    If the item is not registered in the freezer at the moment, it automatically has a zero amount.
    """
    name = models.CharField(max_length=45, verbose_name="food item")
    category = models.ForeignKey(FoodCategory, null=True, on_delete=models.SET_NULL)  # FoodItems are expected to have a category. However, deleting a category does not delete all the items, they stay without category
    currently_registered = models.BooleanField(verbose_name="currently registered", default=True) # specifies whether the existing item is currently listed in the freezer
    amount = models.IntegerField(verbose_name="food amount", default=0)

    def __str__(self):
        return f'{self.name} ({self.category}) - amount: {self.amount}'

    class Meta:
        verbose_name = "Food item"
        verbose_name_plural = "Food items"
