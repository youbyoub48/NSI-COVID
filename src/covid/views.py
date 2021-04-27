from django.shortcuts import render, HttpResponse

import API

# Create your views here.
def covid(request, Pays="France", mode="deaths", jours=30):
    days, data = API.Multi_Pays(pays=Pays.split(","), mode=mode, jours=jours)
    return render(request, "covid/dashboard.html", context={"Data": data, "days_labels": days, "Mode":mode})