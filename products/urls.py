from django.urls import path,include
from products import views

urlpatterns = [
    path('',views.base,name="base"),
    path('index/',views.index,name="home"),
    path('details/<int:pk>/',views.details,name="details"),
    path('list/',views.list,name="list"),
    path('add/',views.add,name='add'),
    path('edit/<int:pk>/',views.edit,name="edit"),
    path('delete/<int:pk>/',views.delete, name="delete"),
]