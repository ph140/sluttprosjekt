# Importerer nødvendige bibliotek
from matplotlib import pyplot as plt
import numpy as np
from itertools import count

# Konstanten 3.27 passer best med målingen jeg gjorde.
k0 = 3.27


h = 10  # Hoyde/m
radius_torn = 17  # Radius/m
radius_propp = 1.24  # Radius/m

A = radius_torn**2*np.pi  # Areal propp/m^2
Ap = radius_propp**2*np.pi  # Areal grunnflate/m^2

# Utrykk for k
k = k0*(Ap/A)


def waterchange(h):
    # Funskjon for endring av vannhoyde
    return -k*np.sqrt(h)


# Definere lister som trengs
time = [0]  # Tid/ms
model = [h]  # Hoyde/m

# Uendelig loop, i inkrementerer
for i in count(0):
    # Avslutter dersom vannstanden har nådd halveis
    if model[i] < 0.0000001:
        break

    # Eulers metode. Deler på 1000 for bedre nøyaktighet
    model.append(model[i] + waterchange(model[i]))
    time.append(i+1)

# Skriver hvor lang tid det tar
print(f'Halveis etter {time[-1]} sekunder')

# Plotter grafen
plt.plot(time, model, 'r-')
plt.xlabel('Tid/ms')
plt.ylabel('Vannstand/m')
plt.show()
