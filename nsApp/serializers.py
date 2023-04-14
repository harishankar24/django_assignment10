from .models import Customer, Order
from rest_framework.serializers import ModelSerializer


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerSerializer(ModelSerializer):
    orders = OrderSerializer(read_only=True, many=True)
    class Meta:
        model = Customer
        fields = '__all__'