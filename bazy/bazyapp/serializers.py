from rest_framework import serializers
from .models import Kurs, Uczestnik

class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = '__all__'

class UczestnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uczestnik
        fields = '__all__'
