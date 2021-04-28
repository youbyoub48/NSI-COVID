from datetime import date, timedelta
import requests
import json

def Covid_Pays(pays, mode, jours=30):
    debut_date = date.today() - timedelta(days=1)
    fin_date = debut_date - timedelta(days=jours)
    get = requests.get(f"https://api.covid19api.com/total/country/{pays}/status/{mode}?from={fin_date}T00:00:00Z&to={debut_date}T00:00:00Z")
    if not get and not get.json():
        return False, False
    get = get.json()
    liste_cases = []
    liste_date = []
    for i in range(jours):
        Date = get[i]["Date"]
        Date = Date[:10]
        liste_date.append(Date)
        Cases = get[i]["Cases"]
        liste_cases.append(Cases)
    return liste_date, liste_cases


def Multi_Pays(pays, mode, jours=7):
    liste_cases = []
    api_data = {}
    for line in pays:
        Date, cases = Covid_Pays(pays=line,mode=mode,jours=jours)
        liste_cases.append(cases)
    x = 0
    for line in pays:
        Cases = liste_cases[x]
        api_data[line] = Cases
        x += 1
    return Date, api_data
            


if __name__ == "__main__":
    #print(json.dumps(Covid_Pays("france","confirmed",jours=7), indent=4))
    print(json.dumps(Multi_Pays(pays=["France","South-Africa"],mode="confirmed"), indent=4))