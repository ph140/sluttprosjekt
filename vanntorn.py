# Importerer nødvendige bibliotek
from xlwt import Workbook  # for excel
import xlwt  # for excel
import numpy as np
from itertools import count

# Konstanten 3.27 passer best med målingen jeg gjorde.
k0 = 3.27
diameter_basseng = 10  # Diameter/m
diameter_propp = 1  # Diameter/m
A = (diameter_basseng/2)**2*np.pi  # Areal propp/m^2
Ap = (diameter_propp/2)**2*np.pi  # Areal grunnflate/m^2
k = k0*(Ap/A)  # Uttrykk for k


def waterchange(h):
    # Funskjon for endring av vannhoyde
    return -k*np.sqrt(h)


# Initialiserer en arbeidsbok i excel, som skal fylles med data
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

for j in range(50):
    h = 1+j*10  # Hoyde/m  Kjører gjennom 50 forskjellige verdier

    # Definere lister som trengs
    time = [0]  # Tid/ms
    model = [h]  # Hoyde/m

    # Uendelig loop, i inkrementerer.
    for i in count(0):
        # Avslutter dersom vannstanden er under 0.5 meter
        if model[i] < 0.5:
            break

        # Eulers metode. Deler på 10 for større nøyaktighet
        model.append(model[i] + waterchange(model[i])/10)  # Eulers metode
        time.append(i+1)

    # Skriver ut informasjonen til excel
    sheet1.write(j, 0, str(time[-1]/10))  # Tid kolonne 1
    sheet1.write(j, 1, str(h))  # Vannstand kolonne 2

wb.save('example.xls')  # Lagrer excel-dokumentet
