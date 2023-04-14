from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CustomerListView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer