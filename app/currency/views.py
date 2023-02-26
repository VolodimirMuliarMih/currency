from django.http import HttpResponse
from django.shortcuts import render
from currency.models import Rate, ContactUs


def list_rates(request):
    qs = Rate.objects.all()
    result = []
    for rate in qs:
        result.append(
            f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, currency: {rate.currency}, source: {rate.source}, created: {rate.created} <br>')
    return HttpResponse(str(result))


def LContactUs(request):
    qs = ContactUs.objects.all()
    result = []
    for rate in qs:
        result.append(
            f'id:{rate.id}, email_from:{rate.email_from}, subject:{rate.subject}, massage:{rate.massage} <br>')
    return HttpResponse(str(result))


def tmplContactUs(request):
    contact = ContactUs.objects.all()
    context = {'contact': contact}
    return render(request, 'contact_us.html', context)


def tmpllist_rates(request):
    base = Rate.objects.all()
    context = {'base': base}
    return render(request, 'rates.html', context)
