from django.urls import path
from petstoreapp import views
from django.conf.urls.static import static
from petstore import settings

app_name='petstoreapp'

urlpatterns = [
    path('pets/', PetListView.as_view()),
    path('petlist/'views.pet_list_view),
    path('rangelist/',views.pet_range_list_view),
    path('doglist/',views.DogListView.as_view()),
    path('catlist/',views.CatListView.as_view()),
    #path('<pk>/', views.PetDetailView.as_view()),
    path('/<slug:slug>/', views.PetDetailSlugView.as_view(),name='detail'),
    
    #path('<pk>',views.pet_detail_view),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
