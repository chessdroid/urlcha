from rest_framework.views import APIView
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .serializers import UrlSerializer
from  .utils import hash_function
from .models import UrlModel
from django.http import HttpResponse

class MainView(APIView):

	def get(self, request, format=None):
		obj  = UrlModel.objects.get(pk='qJZX4MmG')
		serializer = UrlSerializer(obj)
		return Response(serializer.data)

	def post(self, request):
		data = request.data
		url = data.get("url")
		if url.startswith('https://'):
			url = url[8:]
		if url.startswith('http://'):
			url = url[7:]

		small_url = hash_function(url)
		obj, created = UrlModel.objects.get_or_create(pk=small_url, defaults={'url': url})
		serializer = UrlSerializer(obj)
		return Response(serializer.data)

class Redirector(APIView):
    
	def get(self, request, small_url):
		data = request.data
		obj = UrlModel.objects.get(pk=small_url)
		try:
			redirect_url = obj.url
			response = HttpResponse("", status=302)
			response['Location'] = "http://" + redirect_url
			return response
		except:
			return Response(status_code=404)