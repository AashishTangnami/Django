
 #this is where we set up urls to redirect.

from django.contrib import admin
from django.urls import path, include #include lets a new url to include of an app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes.urls')), #this is the first url that program checks

]
