
from rest_framework import serializers
from . models import RequestForm

class RequestFormSerializers(serializers.ModelSerializer):
	class Meta:
		model=RequestForm
		fields='__all__'