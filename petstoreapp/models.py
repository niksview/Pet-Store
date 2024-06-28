from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class PetQuerySet(models.QuerySet):
    def dog_list(self):
        return self.filter(animal_type='D')

    def cat_list(self):
        return self.filter(animal_type='C')

#class CustomManager(models.Manager):        

class CustomManager(models.Manager):
    def get_queryset(self, r1, r2):
        return super().get_queryset().filter(price_range=(r1, r2)) #order_by('name')

    def dog_list(self):
        return self.get_queryset().dog_list()

    def cat_list(self):
        return self.get_queryset().cat_list()

class Pet(models.Model):
    gender =(("male","male"),("female","female"))
    type=(("D","Dog"),("C","Cat"))
    image=models.ImageField(upload_to='media')
    name=models.CharField(max_length=30, verbose_name="Name:")
    price=models.FloatField(default="10")
    animal_type=models.CharField(max_length=30,choices=type)
    species=models.CharField(max_length=30, verbose_name="Species:")
    breed=models.CharField(max_length=30, verbose_name="Breed:")
    age=models.IntegerField()
    gender=models.CharField(max_length=30,choices=gender,verbose_name="Gender")
    description=models.CharField(max_length=400, verbose_name="Description")
    objects=models.Manager()
    pets=CustomManager()
    pet=PetQuerySet.as_manager()
    slug=models.SlugField(max_length=30,null=True)


def pets_pre_save_receiver(sender, instance, *args, **kwargs):
    print("pets_pre_save_receiver")
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        print(instance.slug)

    pre_save.connect(pets_pre_save_receiver, sender=Pet)

class Meta:
     db_table= "Pet"


    # def __str__(self):
    #     return self.name
