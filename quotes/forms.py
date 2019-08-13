from django import forms
from .models import Stock

class StockForm(forms.modelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]
