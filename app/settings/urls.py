from django.contrib import admin
from django.urls import path
from currency.views import listContactUs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/email/', listContactUs)
]
