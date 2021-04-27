from django.shortcuts import render, HttpResponse

import API

# Create your views here.
def covid(request):
    days, data = API.Multi_Pays(pays=["France"], mode="deaths", jours=30)
    data = data["France"]
    return render(request, "covid/dashboard.html", context={"data": data, "days_labels": days})