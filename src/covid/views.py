from django.shortcuts import render, HttpResponse

import API
import data

# Create your views here.
def covid(request, Pays="France", mode="deaths", jours=30):
    days, data = API.Multi_Pays(pays=Pays.split(","), mode=mode, jours=jours)
    jours_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(jours, "Personnalisé")
    mode_fr = {"deaths": "Morts", "confirmed": "Cas Confirmé", "recovered": "Guéris"}.get(mode)
    return render(request, "covid/dashboard.html", context={"Data": data, "days_labels": days, "mode_fr":mode_fr, "jours_label": jours_label, "Pays":Pays, "Mode":mode, "jours":jours})


def index(request):
    return render(request, "covid/index.html")

def pays(request):
    Pays = sorted(data.p)
    return render(request, "covid/pays.html", context={"Pays":Pays})