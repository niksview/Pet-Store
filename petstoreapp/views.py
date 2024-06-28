from .models import Pet
from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User

from django.views.generic import ListView

def mymodel_list(request):
    return render(request, 'mymodel_list.html')

class PetListView(ListView):
    queryset=Pet.objects.all()
    template_name="petstoreapp/list.html"

class PetDetailView(PetListView):  #DetailView
    queryset=Pet.objects.all()
    print("default Manager",queryset)
    pet_data=Pet.pets.all()
    print("custom Manager",pet_data)
    template_name="petstoreapp/details.html"

    def get_context_data(self, *args, **kwargs):
        context=super(PetDetailView,self).get_context_data(*args, **kwargs)
        #print(context)
        return context
        # qs= Pet.objects.filter(id=pk)
        # if qs.exists() and qs.count()==1:
        #     instance=qs.first()
        # else:
        #     raise Http404("Pet doesn't exist")

        # context={
        #     'object':instance
        # }
        # return render(request, "petstoreapp/details.html",context)
    
    def pet_range_list_view(request):
        queryset=Pet.pets.get_pets_price_range(10000, 20000)
        context={
            'object_list':queryset
        }
        return render(request,"petstoreapp/list.html", context)

class DogListView(ListView):
    template_name="petstoreapp/list.html"

    def get_queryset(self, *args, **kwargs):
        return Pet.pet.dog_list()

class CatListView(ListView):
    template_name="petstoreapp/list.html"

    def get_queryset(self, *args, **kwargs):
        return Pet.pet.cat_list()

def get_object(self, *args, **kwargs):
    request=self.request
    print(request)
    slug=self.kwargs.get('slug')
    print("slug",slug)
    # instance=get_object_or_404(Pet, slug=slug, active=True)
    try:
        instance=Pet.objects.get(slug=slug)
        print(instance)
    except Pet.DoesNotExist:
        raise Http404("Not found..")
    except Pet.MultipleObjectsReturned:
        qs=Pet.objects.filter(slug=slug)
        instance=qs.first()
    except Exception as e:
        raise Http404("Error ",e)
    return instance

