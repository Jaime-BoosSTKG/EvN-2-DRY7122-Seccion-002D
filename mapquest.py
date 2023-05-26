from time import time, ctime
current_DateTime = time()
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "CWEcskfST8Tz8Bbw5AcV0KhVlidjADp9"

while True:
    orig = input("locación Incial: ")
    if orig == "Clouse" or orig == "a":
        break
    dest = input("Destino: ")
    if dest == "Clouse" or dest == "a":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("Estado de la API: " + str(json_status) + " = Esta correcta.\n")
        print("=============================================")
        print("Direcciones desde: " + (orig) + " a " + (dest))
        print("Duración del viaje: " + (json_data["route"]["formattedTime"]))
        print("Kilometros: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print('Hoy es: ',ctime(current_DateTime))
        print("=============================================")
