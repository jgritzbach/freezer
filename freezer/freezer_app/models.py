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