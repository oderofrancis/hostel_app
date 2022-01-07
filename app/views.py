from django.shortcuts import render,redirect
from django.core.serializers import serialize
from django.http import HttpResponse
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

	hostel = serialize('geojson',Hostel.objects.all())
	data = gpd.read_file(hostel)
	total = data[data.columns[2]].sum()

	data = data[['hostel_name',data.columns[2]]].groupby('hostel_name').sum()

	data = data.reset_index()
	data.columns=['hostel','number']

	data = data.sort_values(by='number',ascending=False)
	data_values = data['number'].values.tolist()
	data_names = data['hostel'].values.tolist()


	context = {'total':total,'data_names':data_names,'data_values':data_values}

	return render(request,'user/dashboard.html',context)

def hostel(request):
	hostel = serialize('geojson',Hostel.objects.all())
	return HttpResponse(hostel,content_type='application/json')