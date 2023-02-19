from django.http import HttpResponse
from currency.models import ContactUs
from currency.models import Rate


def list_rates(request):
    qs = Rate.objects.all()
    result = []
    for rate in qs:
        result.append(
            f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, currency: {rate.currency}, source: {rate.source}, created: {rate.created} <br>')
    return HttpResponse(str(result))


def listContactUs(request):
    qs = ContactUs.objects.all()
    result = []
    for rate in qs:
        result.append(
            f'id:{rate.id}, email_from:{rate.email_from}, subject:{rate.subject},'
            f' massage:{rate.massage} <br>')
    return HttpResponse(str(result))

# Create your views here.
