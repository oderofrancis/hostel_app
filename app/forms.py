from django.contrib.gis import forms as geoforms
from django import forms
from .models import *

class HostelForm(forms.ModelForm):

    class Meta:
        model = Hostel
        fields =(
        	"hostel_name","gender",
        	"maximum_capacity","price","location")

        widgets = {'location':  geoforms.OSMWidget(
            attrs={
            'map_width': 330, 
            'map_height': 400,
            'default_lat': -0.4001,
            'default_lon': 36.9576,
            'default_zoom':14,
            'max_zoom':20,
            'min_zoom':3,
            
            })}