from django.shortcuts import render

from .models import Greeting
from .forms import EasterInputForm
from .forms import JulianInputForm

from .astrocalcs import easter_date, julianDate, modifiedJulianDate

# Create your views here.


def index(request):
    return render(request, "index.html")


def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def easter_view(request):
    result = None

    if request.method == 'POST':
        form = EasterInputForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            m, day = easter_date(year)
            month = "March" if m==3 else "April" 
            result = f"Sunday, {month} {int(day)}, {int(year)}"
    else:
        form = EasterInputForm()

    return render(request, 'easter.html', {'form': form, 'result': result})

def julian_view(request):
    result = None

    if request.method == 'POST':
        form = JulianInputForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            day = form.cleaned_data['day']
            hour = form.cleaned_data['hour']
            minute = form.cleaned_data['minute']
            seconds = form.cleaned_data['seconds']
            julian = julianDate(year,month,day,hour,minute,seconds)
            mjd = modifiedJulianDate(year,month,day,hour,minute,seconds)
            result = f"Julian Date {julian}, MJD {mjd}"
    else:
        form = JulianInputForm()

    return render(request, 'juliandates.html', {'form': form, 'result': result})
