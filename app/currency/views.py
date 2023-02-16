from django.shortcuts import render
from django.http import HttpResponse
from currency.models import ContactUs
def listContactUs(request):
    qs = ContactUs.objects.all()
    result = []
    for rate in qs:
        result.append(f'id:{rate.id}, email_from:{rate.email_from}, subject:{rate.subject}, massage:{rate.massage} <br>')
    return HttpResponse(str(result))


# Create your views here.
