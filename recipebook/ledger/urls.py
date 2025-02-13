from django.urls import path

from .views import ledger

urlpatterns = [
    path('', ledger, name='ledger')
]

app_name = "ledger"