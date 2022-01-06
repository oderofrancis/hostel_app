from django.shortcuts import render,redirect
from django.core.serializers import serialize
from .models import *
from .forms import *
import geopandas as gpd
from django.contrib import messages

# Create your views here.


def home(request):

	form = HostelForm()
	
	if request.method == 'POST':
		form = HostelForm(request.POST)

		if form.is_valid():
			form.save()

			messages.success(request, 'we are working on the incidence reported,THANK YOU.')
			return redirect('/')

		else:

			messages.warning(request, form.errors)
			return redirect('/')

	# Analysis

	hostels = Hostel.objects.all().count()

	# population

	hostel = serialize('geojson',Hostel.objects.all())
	data = gpd.read_file(hostel)
	total = data[data.columns[2]].sum()


	context = {'form':form,'hostels':hostels,'total':total}

	return render(request,'user/home.html',context)

# dashboard

def dashboard(request):
	return render(request,'user/dashboard.html')