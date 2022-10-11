import secrets
import uuid
from django.db import models
from users.models import CustomUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

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
    name = models.CharField(_('name'), max_length=200)
    preferred_name = models.CharField(_('preffered_name'), max_length=200)
    email = models.EmailField(_('email'), max_length=100, default='Please enter your email address')
    contact_preference = models.BooleanField(_('contact_preference'), default=False)
    address = models.CharField(_('address'), max_length=400)
    #postcode = models.CharField(_('postcode'), max_length=10, blank=True)
    year_property_built = models.CharField(_('year_property_built'), max_length=4, blank=True)
    property_type = models.CharField(
        _('property_type'),
        max_length=20,
        choices = PROPERTY_TYPE_CHOICES,
        default = 'Detached',
    )
    property_type_other = models.CharField(
        _('property_type_other'),
        max_length=200,
        blank=True)
    construction_material = models.CharField(
        _('construction_material'),
        max_length=20,
        choices = PROPERTY_CONSTRUCTION_CHOICES,
        default = 'Bricks',
    )
    construction_material_other = models.CharField(
        _('construction_material_other'),
        max_length=200,
        blank=True)
    number_of_people = models.IntegerField(_('number_of_people'), default=1)
    purpose_of_garden = models.CharField(
        _('purpose_of_garden'),
        max_length=50,
        choices = PURPOSE_OF_GARDEN_CHOICES,
        default = 'None',
    )
    area_for_growing_veg = models.CharField(
        _('area_for_growing_veg'),
        max_length=20,
        choices = AREA_FOR_GROWING_VEG_CHOICES,
        default = '<1 sq m',
    )
    average_gardening_hours = models.CharField(
        _('average_gardening_hours'),
        max_length=20,
        choices = AVERAGE_GARDENING_HOURS_CHOICES,
        default = '0-1 hrs',
    )
    total_garden_area = models.CharField(
        _('total_garden_area'),
        max_length=20,
        choices = TOTAL_GARDEN_AREA_CHOICES,
        default = '<10 sq m',
    )
    sealed_garden_area = models.CharField(
        _('sealed_garden_area'),
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '<10%',
    )
    lawn_garden_area = models.CharField(
        _('lawn_garden_area'),
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '<10%',
    )
    lawn_type = models.CharField(
        _('lawn_type'),
        max_length=20,
        choices = LAWN_TYPE_CHOICES,
        default = 'Natural',
    )
    veg_garden_area = models.CharField(
        _('veg_garden_area'),
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '<10%',
    )
    ornamental_plant_garden_area = models.CharField(
        _('ornamental_plant_garden_area'),
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '<10%',
    )
    natural_garden_area = models.CharField(
        _('natural_garden_area'),
        max_length=20,
        choices = PORTION_GARDEN_AREA_CHOICES,
        default = '<10%',
    )
    veg_species = models.CharField(
        _('veg_species'),
        max_length=20,
        choices = VEG_SPECIES_CHOICES,
        default = 'Lettuce',
    )
    veg_species_other = models.CharField(
        _('veg_species_other'),
        max_length=200,
        blank=True)
    raised_beds = models.CharField(
        _('raised_beds'),
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'Yes',)
    compost_use = models.CharField(
        _('compost_use'),
        max_length=20,
        choices = COMPOST_CHOICES,
        default = 'Kitchen',
    )
    compost_frequency = models.CharField(
        _('compost_frequency'),
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3+ times',
    )
    fertiliser_frequency = models.CharField(
        _('fertiliser_frequency'),
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3+ times',
    )
    latest_compost_purchase = models.CharField(
        _('latest_compost_purchase'),
        max_length=200,
        blank=True)
    veg_pesticide = models.CharField(
        _('veg_pesticide'),
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3+ times',
    )
    ornamental_plant_fertiliser = models.CharField(
        _('ornamental_plant_fertiliser'),
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3+ times',
    )
    ornamental_plant_pesticide = models.CharField(
        _('ornamental_plant_pesticide'),
        max_length=20,
        choices = COMPOST_FERTILISER_PESTICIDE_CHOICES,
        default = '3+ times',
    )
    soil_rubble = models.CharField(
        _('soil_rubble'),
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'Yes',)
    soil_rubble_description = models.CharField(
        _('soil_rubble_description'),
        max_length=200,
        blank=True)
    bird_feeders = models.CharField(
        _('bird_feeders'),
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'Yes',)
    pond = models.CharField(
        _('pond'),
        max_length=10,
        choices = YES_NO_CHOICES,
        default = 'Yes',)
    house_sparrow = models.CharField(
        _('house_sparrow'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    goldfinch = models.CharField(
        _('goldfinch'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    robin = models.CharField(
        _('robin'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    wren = models.CharField(
        _('wren'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    domestic_cat = models.CharField(
        _('domestic_cat'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    red_fox = models.CharField(
        _('red_fox'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    hedgehog = models.CharField(
        _('hedgehog'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    slow_worm = models.CharField(
        _('slow_worm'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    frog = models.CharField(
        _('frog'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    mole = models.CharField(
        _('mole'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    house_rat = models.CharField(
        _('house_rat'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    bumblebee = models.CharField(
        _('bumblebee'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    ladybird = models.CharField(
        _('ladybird'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    butterfly = models.CharField(
        _('butterfly'),
        max_length=20,
        choices = ANIMAL_SIGHTING_CHOICES,
        default = 'Daily',
    )
    other_notable_wildlife = models.CharField(
        _('other_notable_wildlife'),
        max_length=200,
        blank=True)   
    soil_sample_label = models.CharField(_('soil_sample_label'), max_length=200, blank=True, editable=False, unique=True) 
    participant_code = models.CharField(_('participant_code'), primary_key=True, default=uuid.uuid4, max_length=50, editable=False)
    sample_1_description = models.CharField(_('sample_1_description'), max_length=200)
    sample_2_description = models.CharField(_('sample_2_description'), max_length=200)
    sample_3_description = models.CharField(_('sample_3_description'), max_length=200)
    sample_4_description = models.CharField(_('sample_4_description'), max_length=200)
    sample_5_description = models.CharField(_('sample_5_description'), max_length=200) 
    agreement = models.BooleanField(_('agreement'), default=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)

    def __str__(self):
        return self.soil_sample_label

    def get_absolute_url(self):
        return reverse('home')

    def get_soil_sample_label(self):
        number = secrets.token_hex(nbytes=4).upper()
        return number

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.soil_sample_label = self.get_soil_sample_label()
        super(Participant, self).save(*args, **kwargs)
    
    
    




