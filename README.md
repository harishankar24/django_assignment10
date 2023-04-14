# django_assignment10
Django DRF: Nested Serializers

Two models used

Customer(firstName, lastName, phone)
and
Orders(product, quantity, customer_id)

A customer can have multiple orders


# Sample Data
```
insert into customer (firstName, lastName, phone) values ('Bastian', 'Caig', '2875195130');
insert into customer (firstName, lastName, phone) values ('Muffin', 'Ingon', '9777186837');
insert into orders (product, quantity, customer_id) values ('Soup V8 Roasted Red Pepper', 7, 1);
insert into orders (product, quantity, customer_id) values ('Syrup - Pancake', 14, 2);
```


