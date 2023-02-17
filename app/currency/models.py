from django.db import models


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=25)  # usd, eur
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=25)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=250)
    massage = models.TextField()


""" Use TextField because message can consist from large str, 
Use max_length 250 in subject, id row automat"""
