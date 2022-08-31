import secrets
import uuid
from django.db import models
from users.models import CustomUser
from django.urls import reverse

# choices

PROPERTY_TYPE_CHOICES = (
    ('detached', 'Detached'),
    ('semidetached', 'Semidetached'),
    ('terraced', 'Terraced house'),
    ('apartment', 'Apartment'),
    ('other', 'Other'),
)

PROPERTY_CONSTRUCTION_CHOICES = (
    ('bricks', 'Bricks/stone walls'),
    ('timber', 'Timber-framed walls'),
    ('other', 'Other'),
)

PURPOSE_OF_GARDEN_CHOICES = (
    ('veg', 'Fruit and vegetable production'),
    ('plants', 'Gardening of ornamental plants'),
    ('natural recreation', 'Recreational activity benefiting from natural environment'),
    ('nonnatural recreation', 'Recreational activity without any relevance of natural environment'),
    ('storage', 'Storage space'),
    ('none', 'No specific use and limited leisure time spent in garden'),
)

AREA_FOR_GROWING_VEG_CHOICES = (
    ('0', '<1 square meter'),
    ('1', '1-2 square meters'),
    ('2', '2-5 square meters'),
    ('5', '5-10 square meters'),
    ('10', '>10 square meters'),
)

AVERAGE_GARDENING_HOURS_CHOICES = (
    ('0', '0-1 hours'),
    ('1', '1-2 hours'),
    ('2', '2-5 hours'),
    ('5', '5-10 hours'),
    ('10', '>10 hours'),
)

TOTAL_GARDEN_AREA_CHOICES = (
    ('0', '<10 square meters'),
    ('10', '10-100 square meters'),
    ('100', '100-200 square meters'),
    ('200', '200-500 square meters'),
    ('500', '>500 square meters'),
)

PORTION_GARDEN_AREA_CHOICES = (
    ('0', '<10%'),
    ('10', '10-20%'),
    ('20', '20-50%'),
    ('50', '50-70%'),
    ('70', '70-100%'),
)

LAWN_TYPE_CHOICES = (
    ('natural', 'Natural'),
    ('artificial', 'Artificial'),
)

VEG_SPECIES_CHOICES = (
    ('lettuce', 'Lettuce'),
    ('spinach', 'Spinach'),
    ('herbs', 'Herbs'),
    ('carrots', 'Carrots'),
    ('potatoes', 'Potatoes'),
    ('onions', 'Onions'),
    ('beans', 'Beans'),
    ('tomatoes', 'Tomatoes'),
    ('apples', 'Apples'),
    ('pears', 'Pears'),
    ('cherries', 'Cherries'),
    ('strawberries', 'Strawberries'),
    ('other', 'Other'),
)

COMPOST_CHOICES = (
    ('kitchen', 'I do compost kitchen waste'),
    ('garden', 'I do compost garden waste'),
    ('both', 'I do compost both kitchen and garden waste'),
    ('none', 'I do NOT compost any kitchen or garden waste'),
)

COMPOST_FERTILISER_PESTICIDE_CHOICES = (
    ('3', '3+ times in the last year'),
    ('1', '1-3 times in the last year'),
    ('occasionally', 'Occasionally in the last 5 years'),
    ('never', 'Not in the last 5 years/never')
)

ANIMAL_SIGHTING_CHOICES = (
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('seasonally', 'Seasonally'),
    ('yearly', 'Yearly'),
    ('never', 'Never'),
    ('unknown', 'Unknown'),
)

YES_NO_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
)


# Create your models here.
class Participant(models.Model):
    user = models.ForeignKey(CustomUser, 
    on_delete=models.CASCADE, 
    default=True, 
    related_name='participant')
    name = models.CharField(max_length=200)
    preferred_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, default=True)
    contact_preference = models.BooleanField(default=False)
    address = models.CharField(max_length=400)
    year_property_built = models.DateField
    property_type = models.CharField(
        max_length=20,
        choices = PROPERTY_TYPE_CHOICES,
        default = 'detached',
    )
    property_type_other = models.CharField(
        max_length=200,
        blank=True)
    construction_material = models.CharField(
        max_length=20,
        choices = PROPERTY_CONSTRUCTION_CHOICES,
        default = 'bricks',
    )
    construction_material_other = models.CharField(
        max_length=200,
        blank=True)
    number_of_people = models.IntegerField(default=1)
    purpose_of_garden = models.CharField(
        max_length=50,
        choices = PURPOSE_OF_GARDEN_CHOICES,
        default = 'none',
    )
    area_for_growing_veg = models.CharField(
        max_length=20,
        choices = AREA_FOR_GROWING_VEG_CHOICES,
        default = '0',
    )
    average_gardening_hours = models.CharField(
        max_length=20,
        choices = AVERAGE_GARDENING_HOURS_CHOICES,
        default = '0',
    )
    total_garden_area = models.CharField(
        max_length=20,
        choices = TOTAL_GARDEN_AREA_CHOICES,
        default = '0',
    )
    sealed_garden_area = models.CharField(
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '0',
    )
    lawn_garden_area = models.CharField(
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '0',
    )
    lawn_type = models.CharField(
        max_length=20,
        choices = LAWN_TYPE_CHOICES,
        default = 'natural',
    )
    veg_garden_area = models.CharField(
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '0',
    )
    ornamental_plant_garden_area = models.CharField(
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '0',
    )
    natural_garden_area = models.CharField(
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '0',
    )
    veg_species = models.CharField(
        max_length=20,
        choices = VEG_SPECIES_CHOICES,
        default = 'lettuce',
    )
    veg_species_other = models.CharField(
        max_length=200,
        blank=True)
    raised_beds = models.CharField(
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'yes',)
    compost = models.CharField(
        max_length=20,
        choices = COMPOST_CHOICES,
        default = 'kitchen',
    )
    commercial_compost = models.CharField(
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3',
    )
    commercial_fertiliser = models.CharField(
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3',
    )
    latest_compost_purchase = models.CharField(
        max_length=200,
        blank=True)
    commercial_pesticide = models.CharField(
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3',
    )
    ornamental_plant_fertiliser = models.CharField(
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3',
    )
    ornamental_plant_pesticide = models.CharField(
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3',
    )
    soil_rubble = models.CharField(
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'yes',)
    soil_rubble_yes = models.CharField(
        max_length=200,
        blank=True)
    bird_feeders = models.CharField(
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'yes',)
    pond = models.CharField(
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'yes',)
    house_sparrow = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    goldfinch = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    robin = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    wren = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    domestic_cat = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    red_fox = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    hedgehog = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    slow_worm = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    frog = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    mole = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    house_rat = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    bumblebee = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    ladybird = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    butterfly = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'daily',
    )
    other_notable_wildlife = models.CharField(
        max_length=200,
        blank=True)   
    #id = models.UUIDField(
     #   primary_key=True,
      #  default=uuid.uuid5,
       # editable=False,
        #unique=True)
    soil_sample_label = models.CharField(max_length=200, blank=True, editable=False) 
    sample_label = models.CharField(primary_key=True, default=uuid.uuid4, max_length=50, editable=False)
    sample_1_description = models.CharField(max_length=200)
    sample_2_description = models.CharField(max_length=200)
    sample_3_description = models.CharField(max_length=200)
    sample_4_description = models.CharField(max_length=200)
    sample_5_description = models.CharField(max_length=200)
    agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    def get_soil_sample_label(self):
        number = secrets.token_hex(nbytes=4).upper()
        return number

    def save(self, *args, **kwargs):
        self.soil_sample_label = self.get_soil_sample_label()
        super(Participant, self).save(*args, **kwargs)
    
    
    




