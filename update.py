import requests
from datetime import datetime, timedelta

yesterday = (datetime.today() - timedelta(days=2)).strftime("%Y%m%d")
mexico_file_name = "https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Confirmados_" + yesterday + ".csv"

mexico_cases = requests.get(mexico_file_name)
try:
    mexico_cases.raise_for_status()
    with open("mexico_cases.csv", 'wb') as f:
        f.write(mexico_cases.content)
    print("Cases Successfully Updated at " + datetime.today().strftime("%m/%d/%Y, %H:%M:%S"))

except requests.exceptions.HTTPError as err:
    print("File could not be updated")
    exit(1)

