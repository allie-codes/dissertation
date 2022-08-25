from django import forms
from .models import Participant
from django.utils.translation import gettext_lazy as _

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        labels = {
            'name': _('Your full name (first name and surname):'),
            'preferred_name': _('Preferred name for correspondence:'),
            'contact_preference': _('Yes, I agree to be contacted again in the future.'),
            'address': _('Address of property/soil samples (house no., street name, post code):'),
            'year_property_built': _('Year property was built (approximate if unknown):'),
            'property_type_other': _('If you selected "other," please tell us the property type:'),
            'construction_material_other': _('If you selected "other," please tell us the construction material type:'),
            'number_of_people': _('Number of people living on the property:'),
            'purpose_of_garden': _('Main purpose of your garden:'),
            'area_for_growing_veg': _('Garden area used for growing vegetables/fruit:'),
            'average_gardening_hours': _('Average number of hours per week spent gardening during the peak season (most active household member):'),
            'total_garden_area': _('Total garden area in square meters:'),
            'sealed_garden_area': _('Portion of garden area sealed (e.g., patio/paving/parking):'),
            'lawn_garden_area': _('Portion of garden area covered by lawn:'),
            'lawn_type': _('Type of lawn:'),
            'veg_garden_area': _('Portion of garden area used for growing vegetables/fruit:'),
            'ornamental_plant_garden_area': _('Portion of garden area used for growing ornamental plants:'),
            'natural_garden_area': _('Portion of garden area covered by natural/wild vegetation:'),
            'veg_species': _('Main species of vegetable/fruits grown in your garden:'),
            'veg_species_other': _('If you selected "other," please tell us the main species of vegetables/fruit grown in your garden:'),
            'raised_beds': _('If you grow vegetables, are you using raised beds?'),
            'compost': _('Do you compost your kitchen and garden waste for use in your garden?'),
            'commercial_compost': _('How often have you used commercial compost/manure in your garden?'),
            'commerical_fertiliser': _('How often have you used commercial fertiliser for fruit/vegetables?'),
            'latest_compost_purchase': _('If feasible, provide details of the type and source of your latest compost/manure purchase:'),
            'commercial_pesticide': _('How often have you used commercial pesticides for fruit/vegetables?'),
            'ornamental_plant_fertiliser': _('How often have you used commercial fertiliser for ornamental plants?'),
            'ornamental_plant_pesticide': _('How often have you used commercial pesticides for ornamental plants?'),
            'soil_rubble': _('Have you ever found building waste/rubble in your soil?'),
            'soil_rubble_yes': _('If yes, please describe the rubble you found:'),
            'bird_feeders': _('Do you use bird feeders in your garden?'),
            'pond': _('Do you have a pond in your garden?'),
            'house_sparrow': _('Do you see house sparrows in your garden? If yes, how often during the peak season?'),
            'goldfinch': _('Do you see goldfinches in your garden? If yes, how often during the peak season?'),
            'robin': _('Do you see robins in your garden? If yes, how often during the peak season?'),
            'wren': _('Do you see wrens in your garden? If yes, how often during the peak season?'),
            'domestic_cat': _('Do you see domestic cats in your garden? If yes, how often during the peak season?'),
            'red_fox': _('Do you see red foxes in your garden? If yes, how often during the peak season?'),
            'hedgehog': _('Do you see hedgehogs in your garden? If yes, how often during the peak season?'),
            'slow_worm': _('Do you see slow worms in your garden? If yes, how often during the peak season?'),
            'frog': _('Do you see frogs or toads in your garden? If yes, how often during the peak season?'),
            'mole': _('Do you see moles in your garden? If yes, how often during the peak season?'),
            'house_rat': _('Do you see house rats in your garden? If yes, how often during the peak season?'),
            'bumblebee': _('Do you see bumblebees in your garden? If yes, how often during the peak season?'),
            'ladybird': _('Do you see ladybirds in your garden? If yes, how often during the peak season?'),
            'butterfly': _('Do you see butterflies in your garden? If yes, how often during the peak season?'),
            'other_notable_wildlife': _('Any other notable animal/wildlife observations in your garden during the last year:'),
            'sample_1_description': _('Please provide a description of your <b>soil sample #1</b>: label on bag, sample location (front, back most distant to building, veggie patch 1, veggie patch 2), distance to house:'),
            'sample_2_description': _('Please provide a description of your <b>soil sample #2</b>: label on bag, sample location (front, back most distant to building, veggie patch 1, veggie patch 2), distance to house:'),
            'sample_3_description': _('Please provide a description of your <b>soil sample #3</b>: label on bag, sample location (front, back most distant to building, veggie patch 1, veggie patch 2), distance to house:'),
            'sample_4_description': _('Please provide a description of your <b>soil sample #4</b>: label on bag, sample location (front, back most distant to building, veggie patch 1, veggie patch 2), distance to house:'),
            'sample_5_description': _('Please provide a description of your <b>soil sample #5</b>: label on bag, sample location (front, back most distant to building, veggie patch 1, veggie patch 2), distance to house:'),
            'agreement': _('I agree to participate in the EcoGardenHealth study.')
        }
        help_texts = {
            'contact_preference': _('</br> Please tick this box if you are happy for us to contact you again for further questions and samples (in the future, we are planning to examine veg and invertebrate/biological samples from gardens, too.'),
            'agreement': _('<br> Please tick this box to indicate that you agree to participate in the soil testing project.')
        }
    

