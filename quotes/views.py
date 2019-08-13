from django.shortcuts import render ,redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request): #pk_ce2be8df46d047d399aaba738ba40486 api token public key
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_ce2be8df46d047d399aaba738ba40486")
		try:
			api= json.loads(api_request.content)
		except Exception as e:
			api = "Error!"
		return render(request,' home.html',{'api' :api})
	else:
		return render(request, 'home.html',{'ticker':" Enter a ticker symbol above!"})



	# return render(request, 'home.html',{'api':api}) #this will get the file .html from templates.

def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	import requests
	import json
	if request.method == 'POST':
		# ticker = request.POST['ticker']
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock Has Been Added"))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_ce2be8df46d047d399aaba738ba40486")
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error!"

		return render(request, 'add_stock.html',{'ticker': ticker,'output':output })


def delete(request,stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ('Stock deleted'))
	return redirect('add_stock')
def delete_stock(request):
	ticker = Stock.objects.all()
	retunr render(request, 'delete_stock.html',{'ticker':ticker})
