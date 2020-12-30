from rest_framework import serializers

from hookah.models import Hookah


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hookah
        fields = ('name')