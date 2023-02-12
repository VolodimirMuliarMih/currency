from django.db import models


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=250)
    massage = models.TextField()


""" Use TextField because message can consist from large str, 
Use max_length 250 in subject, id row automat"""
