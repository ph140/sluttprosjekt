# Importerer nødvendige bibliotek
# from matplotlib import pyplot as plt

# Konstanter
gravitational_constant = 6.67408E-11  # m^3 kg^-1 s^-2
earth_mass = 5.972E24  # Mass/kg
earth_radius = 6371000
rocket_mass = 5E5  # Mass/kg


# Variabler
fuel_mass = 8000  # Mass/kg
total_mass = fuel_mass + rocket_mass


# Lager lister
altitude = []
field_strength = []


class Rocket():
    def __init__(self, altitude, velocity, acceleration, mass,
                 methane, LOX, fuel):
        self.altitude = altitude
        self.velocity = velocity
        self.acceleration = acceleration  # Akselerasjon
        self.mass = mass  # Masse
        self.methane = methane  # Flytende metan
        self.LOX = LOX  # Flytende oksygen
        self.fuel = fuel
        self.throttle = 0

    def acceleration(cls):
        return (gravity(cls.altitude) + thrust())/cls.mass

    def thrust(cls):
        return cls.throttle * 2.21E6  # Kraft av motorene / Newton


raptor = Rocket(0, 0, 0, rocket_mass, 0, 0, fuel_mass)


# Funksjoner
def gravity(h):
    """
    Beregner gravitasjonskraften mellom raketten og jorden ved hjelp av Newtons
    universelle gravitasjonslov (k*m1*m2/r^2). Tar inn h som høyde over bakken,
    r blir da jordas radius pluss h.

    """
    return gravitational_constant * total_mass * earth_mass/(earth_radius+h)**2


def thrust():
    return


print(raptor.mass)

# for i in range(1000000):
#     altitude.append(i)
#     field_strength.append(gravity(i)/total_mass)
#
# plt.plot(altitude, field_strength, 'r')
# plt.show()
