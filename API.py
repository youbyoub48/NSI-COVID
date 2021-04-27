from datetime import date, timedelta
import requests
import json

def Covid_Pays(pays, mode, jours=30):
    debut_date = date.today()
    fin_date = debut_date - timedelta(days=jours)
    get = requests.get(f" https://api.covid19api.com/total/country/{pays}/status/{mode}?from={fin_date}T00:00:00Z&to={debut_date}T00:00:00Z ")
    if not get and not get.json():
        return False, False
    get = get.json()
    api_data = {}
    for i in range(jours):
        Date = get[i]["Date"]
        Date = Date[:10]
        Cases = get[i]["Cases"]
        api_data[Date] = Cases
    return api_data


def Multi_Pays(pays, mode, jours=7):
    for line in pays:
        print(json.dumps(Covid_Pays(pays=line,mode=mode,jours=jours), indent=4))
    


if __name__ == "__main__":
    #print(json.dumps(Covid_Pays("france","confirmed",jours=7), indent=4))
    Multi_Pays(pays=["France","South-Africa"],mode="confirmed")