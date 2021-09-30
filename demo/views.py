from django.shortcuts import render
from .models import Person
from rest_framework.views import APIView
from rest_framework.response import Response
from django_dah.dash_app_code import new_plot
from django.http import HttpResponseRedirect
from datetime import datetime 
# Create your views here.
class NameViews(APIView):

	#def get(self,request):
	#	return Response('OK')

	def post(self,request):
		print(self.request.data)
		payload = self.request.data
		name = payload['name']
		income = payload['income']
		age = payload['age']
		hometown = payload['hometown']
		zipcode = payload['zipcode']
		city = payload['city']
		timestamp = payload['timestamp']
		date = datetime.utcfromtimestamp(float(timestamp))

		Person.objects.get_or_create(
			name = name,
			income = income,
			age = age,
			hometown = hometown,
			zipcode = zipcode,
			city = city,
			date = date,
			)

		return Response('OK')



class Analytics(APIView):
	def post(self,request):
		payload = self.request.data
		name = payload['name']
		print(payload)
		new_plot(name)
		return HttpResponseRedirect('/dash_plot')