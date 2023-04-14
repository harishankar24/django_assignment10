from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

    class Meta:
        db_table = 'customer'


class Order(models.Model):
    product = models.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField(default=1)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'