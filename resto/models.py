from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField(max_length=1000)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email






    