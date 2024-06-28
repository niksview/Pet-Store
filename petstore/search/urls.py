from django.urls import path
from .views import DogsListView,CatsListView,SearchPetView

urlpatterns = [
    path('dog_list/', DogsListView.as_view(),name='Doglist'),
    path('cat_list/', CatsListView.as_view(),name='Catlist'),
    
    path('searchview/', SearchPetView.as_view()),
   
]