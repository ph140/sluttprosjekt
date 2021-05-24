def tid(h):
    return 0.0000040593*h**5 - 0.0006141459*h**4 + 0.036044*h**3 - 1.0737*h**2 + 22.768913*h + 0.6582


while True:
    h = int(input('Hvor høy er vannstanden?\n'))
    print(f'Vannstanden når 0.5 meter om {tid(h)} sekunder')
