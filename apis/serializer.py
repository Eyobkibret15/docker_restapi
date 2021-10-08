from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from .models import country, city, hotel

from rest_framework import serializers

class hotelserializer(ModelSerializer):
    class Meta:
        model = hotel
        fields = ["hotel","price","city"]

    # def to_representation(self, instance):
    #     rep = super(hotelserializer, self).to_representation(instance)
    #     rep["city"] = instance.city.city
    #     return rep

class cityserializer(ModelSerializer):
    # values = RelatedFieldAlternative(queryset=value.objects.all(), serializer=valueserializers)
    hotels = hotelserializer(read_only=True)
    # hotels = serializers.StringRelatedField(many=True)
    class Meta:
        model = city
        fields = ["city","level","country","hotels"]

    # def to_representation(self, instance):
    #     rep = super(cityserializer, self).to_representation(instance)
    #     rep["country"] = instance.country.country
    #     return rep

class countryserializer(ModelSerializer):
    citys = cityserializer(many=True, read_only=True)
    # citys = serializers.StringRelatedField(many=True)
    class Meta:
        model = country
        fields = ["country","citys"]
