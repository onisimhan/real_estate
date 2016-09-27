from rest_framework import serializers
from realestate.models import Main, MainRemoved
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class MainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Main
        fields = ('id', 'state', 'city', 'zip_code', 'address', 'get_url')


class MainRemovedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainRemoved
        fields = ('mainid', 'state', 'city', 'zip_code',
                  'address', 'get_url', 'removed_at')

class MainAdvancedSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Main
        fields = ('id', 'state', 'city', 'zip_code', 'address', 'get_url', 'bedrooms', 'bathrooms_full', 'bathrooms_half', 'description', 'features', 'price', 'square_feet', 'square_feet_lot', 'home_type', 'longitude', 'latitude', 'available', 'date_posted', 'create_date', 'get_image_urls')
