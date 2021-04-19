# Importerer nødvendige bibliotek
# from matplotlib import pyplot as plt
import math

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
    def __init__(self, position_x, position_y, velocity_x, velocity_y,
                 acceleration_x, acceleration_y, mass, methane, LOX, fuel):
        self.position_x = position_x  # Posisjon/m
        self.position_y = position_y  # Posisjon/m
        self.velocity_x = velocity_x  # Hastighet/ m/s
        self.velocity_y = velocity_y  # Hastighet/ m/s
        self.acceleration_x = acceleration_x  # Akselerasjon m/s^2
        self.acceleration_y = acceleration_y  # Akselerasjon m/s^2
        self.mass = mass  # Masse
        self.fuel = fuel
        self.throttle = 0
        self.pitch = math.pi/2

    def acceleration(cls):
        return (gravity(cls.altitude) + thrust())/cls.mass

    def thrust(cls):
        return cls.throttle * 2.21E6  # Kraft av motorene / Newton


class Engine():
    def __init__(self, angle):
        self.throttle = 0
        self.angle = angle

    def thrust(cls):
        return cls.throttle * 2.21E6  # Kraft av motorene / Newton


raptor1 = Engine(0, 0, 0, rocket_mass, 0, 0, fuel_mass)
raptor2 = Engine(0, 0, 0, rocket_mass, 0, 0, fuel_mass)
raptor3 = Engine(0, 0, 0, rocket_mass, 0, 0, fuel_mass)

hogstad_rocket = Rocket(0, earth_radius, 0, 0, 0, 0, rocket_mass)


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


print(math.sin(0))


# for i in range(1000000):
#     altitude.append(i)
#     field_strength.append(gravity(i)/total_mass)
#
# plt.plot(altitude, field_strength, 'r')
# plt.show()
