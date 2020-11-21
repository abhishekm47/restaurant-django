from django.db import models
from project.models import MenuItem


class Order(models.Model):
    home = "Home Delivery"
    pickup = "Pickup,Fetch"
    status_choices = ((home, "Home Delivery"),(pickup, "Pickup,Fetch") )
    order_type = models.CharField(
        max_length=22, choices=status_choices, default=home)
    resto1 = "Amsterdamseweg 114 Next to Molen, 1182 HH, Amstelveen The Netherlands"
    resto2 = "Piet Mondriaanplein 189-193, 3812 GZ Amersfoort, The Netherlands"
    resto_choices = ((resto1, "Amsterdamseweg 114 Next to Molen, 1182 HH, Amstelveen The Netherlands"),(resto2, "Piet Mondriaanplein 189-193, 3812 GZ Amersfoort, The Netherlands") )
    resto_type = models.CharField(
        max_length=400, choices=resto_choices, default=resto1)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    yes = 1
    no = 0
    check_choices = ((0, "No"),(1, "Yes") )
    check = models.BooleanField(default=False,choices=check_choices)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    menuitem = models.ForeignKey(
        MenuItem, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    none = "none"
    pending = "pending"
    confirmed = "confirmed"
    progress = "Order in Progress"
    ready = "Ready"
    out = "Out for Delivery"
    complete = "Complete"
    status_choices = ((pending, "pending"), (confirmed, "confirmed"),(progress, "In progress"), (ready, "Ready"), (out, "Out for Delivery"), (complete, "Complete") )
    status = models.CharField(max_length=22, choices=status_choices, default=none)
    thirty_min = "30 Minutes"
    fourty_five_min = "45 Minutes"
    sixty_min = "60 Minutes"
    ninty_min = "90 Minutes"
    time_choices = ((thirty_min, "30 Minutes"), (fourty_five_min, "45 Minutes"),(sixty_min, "60 Minutes"), (ninty_min, "90 Minutes") )
    time = models.CharField(
        max_length=22, choices=time_choices, default=thirty_min)


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
