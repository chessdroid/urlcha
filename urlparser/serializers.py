from .models import UrlModel
from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):
	class Meta:
		model  = UrlModel
		fields = '__all__' 
			