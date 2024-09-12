from rest_framework import serializers
from .models import Plan, Promo, UserSelectedPlans

class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    promos = PromoSerializer(many=True)
    class Meta:
        model = Plan
        fields = ['planId', 'planName', 'benefitType', 'benefitPercentage', 'amountOptions', 'tenureOptions', 'promos']

class UserSelectedPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSelectedPlans
        fields = "__all__"