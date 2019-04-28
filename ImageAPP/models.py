from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hotelrooms(models.Model):
    wel_home_text = models.CharField(max_length=50, null=True)
    hotel_name = models.CharField(max_length=50, null=True)
    home_text = models.CharField(max_length=20, null=True)
    learn_text = models.CharField(max_length=20, null=True)
    room_no_text = models.CharField(max_length=20, null=True)
    day_price = models.IntegerField(max_length=20, null=True)
    day_price_dis = models.IntegerField(max_length=20, null=True)
    month_price = models.IntegerField(max_length=20, null=True)
    mont_price_dis = models.IntegerField(max_length=20, null=True)
    profile_text =  models.CharField(max_length=17, blank=True)
    room_flag =  models.CharField(max_length=10, blank=True)


    def __str__(self):
        return self.home_text

class Homepagetext(models.Model):
    hotel_data = models.ForeignKey(Hotelrooms, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel_data


class Signup(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, null=True)
    phone =  models.CharField(max_length=17, blank=True)
    email_id = models.EmailField(blank=True, unique=True)
    date_birth = models.CharField(max_length=10,null=True)
    password = models.CharField(max_length=8,null=True)
    confirm_password = models.CharField(max_length=8,null=True)


    def __str__(self):
        return self.first_name



