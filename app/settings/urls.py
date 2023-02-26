from django.contrib import admin
from django.urls import path
from currency.views import LContactUs,  tmplContactUs, tmpllist_rates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/email/', LContactUs),
    path('contactus/', tmplContactUs),
    path('ratesbase/', tmpllist_rates)
]
