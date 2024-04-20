from django.urls import path
from . import views

urlpatterns = [
    path("", views.Recordset.as_view(), name="recordset"),
    path("record-items/", views.RecordItems.as_view(), name="record-items"),
]