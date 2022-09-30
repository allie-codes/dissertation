import secrets
import uuid
from django.db import models
from users.models import CustomUser
from django.urls import reverse

# choices

PROPERTY_TYPE_CHOICES = (
    ('Detached', 'Detached'),
    ('Semidetached', 'Semidetached'),
    ('Terraced', 'Terraced house'),
    ('Apartment', 'Apartment'),
    ('Other', 'Other'),
)

PROPERTY_CONSTRUCTION_CHOICES = (
    ('Bricks', 'Bricks/stone walls'),
    ('Timber', 'Timber-framed walls'),
    ('Other', 'Other'),
)

PURPOSE_OF_GARDEN_CHOICES = (
    ('Veg', 'Fruit and vegetable production'),
    ('Plants', 'Gardening of ornamental plants'),
    ('Natural Recreation', 'Recreational activity benefiting from natural environment'),
    ('Nonnatural Recreation', 'Recreational activity without any relevance of natural environment'),
    ('Storage', 'Storage space'),
    ('None', 'No specific use and limited leisure time spent in garden'),
)

AREA_FOR_GROWING_VEG_CHOICES = (
    ('<1 sq m', '<1 square meter'),
    ('1-2 sq m', '1-2 square meters'),
    ('2-5 sq m', '2-5 square meters'),
    ('5-10 sq m', '5-10 square meters'),
    ('>10 sq m', '>10 square meters'),
)

AVERAGE_GARDENING_HOURS_CHOICES = (
    ('0-1 hrs', '0-1 hours'),
    ('1-2 hrs', '1-2 hours'),
    ('2-5 hrs', '2-5 hours'),
    ('5-10 hrs', '5-10 hours'),
    ('>10 hrs', '>10 hours'),
)

TOTAL_GARDEN_AREA_CHOICES = (
    ('<10 sq m', '<10 square meters'),
    ('10-100 sq m', '10-100 square meters'),
    ('100-200 sq m', '100-200 square meters'),
    ('200-500 sq m', '200-500 square meters'),
    ('>500 sq m', '>500 square meters'),
)

PORTION_GARDEN_AREA_CHOICES = (
    ('<10%', '<10%'),
    ('10-20%', '10-20%'),
    ('20-50%', '20-50%'),
    ('50-70%', '50-70%'),
    ('70-100%', '70-100%'),
)

LAWN_TYPE_CHOICES = (
    ('Natural', 'Natural'),
    ('Artificial', 'Artificial'),
)

VEG_SPECIES_CHOICES = (
    ('Lettuce', 'Lettuce'),
    ('Spinach', 'Spinach'),
    ('Herbs', 'Herbs'),
    ('Carrots', 'Carrots'),
    ('Potatoes', 'Potatoes'),
    ('Onions', 'Onions'),
    ('Beans', 'Beans'),
    ('Tomatoes', 'Tomatoes'),
    ('Apples', 'Apples'),
    ('Pears', 'Pears'),
    ('Cherries', 'Cherries'),
    ('Strawberries', 'Strawberries'),
    ('Other', 'Other'),
)

COMPOST_CHOICES = (
    ('Kitchen', 'I do compost kitchen waste'),
    ('Garden', 'I do compost garden waste'),
    ('Both', 'I do compost both kitchen and garden waste'),
    ('None', 'I do NOT compost any kitchen or garden waste'),
)

COMPOST_FERTILISER_PESTICIDE_CHOICES = (
    ('3+ times', '3+ times in the last year'),
    ('1-3 times', '1-3 times in the last year'),
    ('Occasionally', 'Occasionally in the last 5 years'),
    ('Never', 'Not in the last 5 years/never')
)

ANIMAL_SIGHTING_CHOICES = (
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),
    ('Seasonally', 'Seasonally'),
    ('Yearly', 'Yearly'),
    ('Never', 'Never'),
    ('Unknown', 'Unknown'),
)

YES_NO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


# Create your models here.
class Participant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=True, related_name='participant')
    name = models.CharField(max_length=200)
    preferred_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, default='Please enter your email address')
    contact_preference = models.BooleanField(default=False)
    address = models.CharField(max_length=400)
    postcode = models.CharField(max_length=10, blank=True)
    year_property_built = models.CharField(max_length=4, blank=True)
    property_type = models.CharField(
        max_length=20,
        choices = PROPERTY_TYPE_CHOICES,
        default = 'Detached',
    )
    property_type_other = models.CharField(
        max_length=200,
        blank=True)
    construction_material = models.CharField(
        max_length=20,
        choices = PROPERTY_CONSTRUCTION_CHOICES,
        default = 'Bricks',
    )
    construction_material_other = models.CharField(
        max_length=200,
        blank=True)
    number_of_people = models.IntegerField(default=1)
    purpose_of_garden = models.CharField(
        max_length=50,
        choices = PURPOSE_OF_GARDEN_CHOICES,
        default = 'None',
    )
    area_for_growing_veg = models.CharField(
        max_length=20,
        choices = AREA_FOR_GROWING_VEG_CHOICES,
        default = '<1 sq m',
    )
    average_gardening_hours = models.CharField(
        max_length=20,
        choices = AVERAGE_GARDENING_HOURS_CHOICES,
        default = '0-1 hrs',
    )
    total_garden_area = models.CharField(
        max_length=20,
        choices = TOTAL_GARDEN_AREA_CHOICES,
        default = '<10 sq m',
    )
    sealed_garden_area = models.CharField(
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '<10%',
    )
    lawn_garden_area = models.CharField(
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '<10%',
    )
    lawn_type = models.CharField(
        max_length=20,
        choices = LAWN_TYPE_CHOICES,
        default = 'Natural',
    )
    veg_garden_area = models.CharField(
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '<10%',
    )
    ornamental_plant_garden_area = models.CharField(
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '<10%',
    )
    natural_garden_area = models.CharField(
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '<10%',
    )
    veg_species = models.CharField(
        max_length=20,
        choices = VEG_SPECIES_CHOICES,
        default = 'Lettuce',
    )
    veg_species_other = models.CharField(
        max_length=200,
        blank=True)
    raised_beds = models.CharField(
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'Yes',)
    compost_use = models.CharField(
        max_length=20,
        choices = COMPOST_CHOICES,
        default = 'Kitchen',
    )
    compost_frequency = models.CharField(
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3+ times',
    )
    fertiliser_frequency = models.CharField(
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3+ times',
    )
    latest_compost_purchase = models.CharField(
        max_length=200,
        blank=True)
    veg_pesticide = models.CharField(
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3+ times',
    )
    ornamental_plant_fertiliser = models.CharField(
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3+ times',
    )
    ornamental_plant_pesticide = models.CharField(
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3+ times',
    )
    soil_rubble = models.CharField(
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'Yes',)
    soil_rubble_description = models.CharField(
        max_length=200,
        blank=True)
    bird_feeders = models.CharField(
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'Yes',)
    pond = models.CharField(
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'Yes',)
    house_sparrow = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    goldfinch = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    robin = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    wren = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    domestic_cat = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    red_fox = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    hedgehog = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    slow_worm = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    frog = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    mole = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    house_rat = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    bumblebee = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    ladybird = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    butterfly = models.CharField(
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    other_notable_wildlife = models.CharField(
        max_length=200,
        blank=True)   
    soil_sample_label = models.CharField(max_length=200, blank=True, editable=False, unique=True) 
    participant_code = models.CharField(primary_key=True, default=uuid.uuid4, max_length=50, editable=False)
    sample_1_description = models.CharField(max_length=200)
    sample_2_description = models.CharField(max_length=200)
    sample_3_description = models.CharField(max_length=200)
    sample_4_description = models.CharField(max_length=200)
    sample_5_description = models.CharField(max_length=200)
    agreement = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.soil_sample_label

    def get_absolute_url(self):
        return reverse('home')

    def get_soil_sample_label(self):
        number = secrets.token_hex(nbytes=4).upper()
        return number

    def save(self, *args, **kwargs):
        self.soil_sample_label = self.get_soil_sample_label()
        super(Participant, self).save(*args, **kwargs)
    
    
    




